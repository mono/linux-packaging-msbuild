#
# spec file for package msbuild
#
# Copyright (c) 2016 Xamarin, Inc (http://www.xamarin.com)
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           msbuild
Version:	15.2+xamarinxplat.2017.04.21.22.45
Release:	0.xamarin.2
Summary:        Build system for .NET projects
License:        MIT
Group:          Development/Libraries/Other
Url:            https://github.com/Microsoft/msbuild
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        msbuild_%{version}.orig.tar.gz
Patch0:		centos_runtime.patch
BuildRequires:  mono-devel
BuildRequires:  libunwind-devel
BuildRequires:  libicu-devel
BuildRequires:  libcurl-devel
BuildArch:      noarch

%description
The Microsoft Build Engine is a platform for building applications.
This engine, which is also known as MSBuild, provides an XML schema
for a project file that controls how the build platform processes
and builds software. Visual Studio uses MSBuild, but MSBuild does
not depend on Visual Studio. By invoking msbuild.exe on your
project or solution file, you can orchestrate and build products
in environments where Visual Studio isn't installed.

%prep
%setup -n msbuild-d15.2-beta-1
%patch0 -p1

%define _use_internal_dependency_generator 0
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/redhat/find-provides && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/redhat/find-requires && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-requires ; } | sort | uniq'
%else
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-provides && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-requires && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-requires ; } | sort | uniq'
%endif

%build
%{?exp_env}
%{?env_options}
./cibuild.sh --scope Compile --host Mono --target Mono

%install
%{?env_options}
DESTDIR=%{buildroot} ./install-mono-prefix.sh %{_prefix}

%files
%defattr(-,root,root)
%_prefix/lib/
%_bindir/*
