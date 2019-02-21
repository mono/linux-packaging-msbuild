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
Version:	16.0+xamarinxplat.2018.09.26.17.53
Release:	0.xamarin.4
Summary:        Build system for .NET projects
Epoch:		1
License:        MIT
Group:          Development/Libraries/Other
Url:            https://github.com/Microsoft/msbuild
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        msbuild-%{version}.tar.xz
Patch0:		fixed-build-version.diff
BuildRequires:  mono-devel
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildArch:      noarch
Requires:       msbuild-libhostfxr

%description
The Microsoft Build Engine is a platform for building applications.
This engine, which is also known as MSBuild, provides an XML schema
for a project file that controls how the build platform processes
and builds software. Visual Studio uses MSBuild, but MSBuild does
not depend on Visual Studio. By invoking msbuild.exe on your
project or solution file, you can orchestrate and build products
in environments where Visual Studio isn't installed.

%package sdkresolver
Summary:        Build system for .NET projects - .NET Core location resolver
License:        MIT
Group:          Development/Libraries/Other

%description sdkresolver
The Microsoft Build Engine is a platform for building applications.
This engine, which is also known as MSBuild, provides an XML schema
for a project file that controls how the build platform processes
and builds software. Visual Studio uses MSBuild, but MSBuild does
not depend on Visual Studio. By invoking msbuild.exe on your
project or solution file, you can orchestrate and build products
in environments where Visual Studio isn't installed. This package
contains components needed to build with .NET Core.

%prep
%setup -n msbuild-16.0
%patch0 -p1

%define _use_internal_dependency_generator 0
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/redhat/find-provides && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/redhat/find-requires && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-requires ; } | sort | uniq | grep -v \\(NuGet.Versioning\\) | grep -v \\(System.Xml.ReaderWriter\\) | grep -v \\(System.IO.Compression\\) | grep -v \\(NuGet.Frameworks\\) | grep -v \\(System.Reflection.Metadata\\) | grep -v \\(System.Net.Http\\) | grep -v \\(System.Composition.TypedParts\\) | grep -v \\(System.Composition.Hosting\\) | grep -v \\(Microsoft.Cci\\) | grep -v \\(NuGet.Common\\) | grep -v \\(System.Security.Cryptography.Algorithms\\) | grep -v \\(System.Xml.XPath.XmlDocument\\) | grep -v \\(NuGet.RuntimeModel\\) | grep -v \\(NuGet.ContentModel\\) | grep -v \\(NuGet.Packaging\\) | grep -v \\(Microsoft.Build.Tasks.Core\\) | grep -v \\(Microsoft.Web.Deployment.Tracing\\) | grep -v \\(Newtonsoft.Json\\) | grep -v \\(System.Runtime.Loader\\) | grep -v \\(xunit.execution.dotnet\\) | grep -v \\(Microsoft.Web.Administration\\) | grep -v \\(NuGet.Client\\) | grep -v \\(System.Composition.Runtime\\) | grep -v \\(Microsoft.Build.Framework\\) | grep -v \\(System.Collections.NonGeneric\\) | grep -v \\(NuGet.ProjectModel\\) | grep -v \\(NuGet.Protocol.Core.v3\\) | grep -v \\(System.Composition.AttributedModel\\) | grep -v \\(xunit.abstractions\\) | grep -v \\(Microsoft.Web.Hosting\\) | grep -v \\(NuGet.Packaging.Core.Types\\) | grep -v \\(Microsoft.Build.Utilities.Core\\) | grep -v \\(System.Security.Cryptography.ProtectedData\\) | grep -v \\(System.Runtime.InteropServices.RuntimeInformation\\) | grep -v \\(System.Text.Encoding.CodePages\\) | grep -v \\(System.Net.Primitives\\) | grep -v \\(System.Net.Requests\\) | grep -v \\(System.ServiceModel.Security\\) | grep -v \\(System.ServiceModel.Primitives\\) | grep -v \\(System.ServiceModel.Duplex\\) | grep -v \\(System.ServiceModel.Http\\) | grep -v \\(xunit.core\\) | grep -v \\(NuGet.Protocol\\) | grep -v \\(System.Security.Principal.Windows\\) | grep -v \\(System.Security.AccessControl\\) | grep -v \\(NuGet.Commands\\) | grep -v \\(NuGet.Configuration\\) | grep -v \\(Microsoft.Build.Tasks.CodeAnalysis\\) | grep -v \\(NuGet.LibraryModel\\) | grep -v \\(System.Data.Common\\) | grep -v \\(System.Globalization.Extensions\\) | grep -v \\(System.Diagnostics.StackTrace\\) | grep -v \\(System.Threading.Overlapped\\) | grep -v \\(System.Security.SecureString\\) | grep -v \\(System.Xml.XPath.XDocument\\) | grep -v 0\\.0\\.0\\.0'
%else
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-provides && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-requires && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-requires ; } | sort | uniq | grep -v \\(NuGet.Versioning\\) | grep -v \\(System.Xml.ReaderWriter\\) | grep -v \\(System.IO.Compression\\) | grep -v \\(NuGet.Frameworks\\) | grep -v \\(System.Reflection.Metadata\\) | grep -v \\(System.Net.Http\\) | grep -v \\(System.Composition.TypedParts\\) | grep -v \\(System.Composition.Hosting\\) | grep -v \\(Microsoft.Cci\\) | grep -v \\(NuGet.Common\\) | grep -v \\(System.Security.Cryptography.Algorithms\\) | grep -v \\(System.Xml.XPath.XmlDocument\\) | grep -v \\(NuGet.RuntimeModel\\) | grep -v \\(NuGet.ContentModel\\) | grep -v \\(NuGet.Packaging\\) | grep -v \\(Microsoft.Build.Tasks.Core\\) | grep -v \\(Microsoft.Web.Deployment.Tracing\\) | grep -v \\(Newtonsoft.Json\\) | grep -v \\(System.Runtime.Loader\\) | grep -v \\(xunit.execution.dotnet\\) | grep -v \\(Microsoft.Web.Administration\\) | grep -v \\(NuGet.Client\\) | grep -v \\(System.Composition.Runtime\\) | grep -v \\(Microsoft.Build.Framework\\) | grep -v \\(System.Collections.NonGeneric\\) | grep -v \\(NuGet.ProjectModel\\) | grep -v \\(NuGet.Protocol.Core.v3\\) | grep -v \\(System.Composition.AttributedModel\\) | grep -v \\(xunit.abstractions\\) | grep -v \\(Microsoft.Web.Hosting\\) | grep -v \\(NuGet.Packaging.Core.Types\\) | grep -v \\(Microsoft.Build.Utilities.Core\\) | grep -v \\(System.Security.Cryptography.ProtectedData\\) | grep -v \\(System.Runtime.InteropServices.RuntimeInformation\\) | grep -v \\(System.Text.Encoding.CodePages\\) | grep -v \\(System.Net.Primitives\\) | grep -v \\(System.Net.Requests\\) | grep -v \\(System.ServiceModel.Security\\) | grep -v \\(System.ServiceModel.Primitives\\) | grep -v \\(System.ServiceModel.Duplex\\) | grep -v \\(System.ServiceModel.Http\\) | grep -v \\(xunit.core\\) | grep -v \\(NuGet.Protocol\\) | grep -v \\(System.Security.Principal.Windows\\) | grep -v \\(System.Security.AccessControl\\) | grep -v \\(NuGet.Commands\\) | grep -v \\(NuGet.Configuration\\) | grep -v \\(Microsoft.Build.Tasks.CodeAnalysis\\) | grep -v \\(NuGet.LibraryModel\\) | grep -v \\(System.Data.Common\\) | grep -v \\(System.Globalization.Extensions\\) | grep -v \\(System.Diagnostics.StackTrace\\) | grep -v \\(System.Threading.Overlapped\\) | grep -v \\(System.Security.SecureString\\) | grep -v \\(System.Xml.XPath.XDocument\\) | grep -v 0\\.0\\.0\\.0'
%endif

%build
%{?exp_env}
%{?env_options}
./build.sh -hostType mono -configuration Release -skipTests -p:DisableNerdbankVersioning=true -p:BUILD_SOURCEVERSION=8af44c5b9e727c096833a88fae05c3ddb76716d0

%install
%{?env_options}
./artifacts/mono-msbuild/msbuild mono/build/install.proj /p:MonoInstallPrefix=%{buildroot}/%_prefix /p:Configuration=Release-MONO /p:IgnoreDiffFailure=true
sed -i "s@%{buildroot}@@g" %{buildroot}/%_prefix/bin/msbuild
find %{buildroot} -name Microsoft.DiaSymReader.Native.*dll -delete
find %{buildroot} -name *.dylib -delete

%files
%defattr(-,root,root)
%_prefix/lib/mono/msbuild/15.0/bin/ru
%_prefix/lib/mono/msbuild/15.0/bin/fr
%_prefix/lib/mono/msbuild/15.0/bin/ja
%_prefix/lib/mono/msbuild/15.0/bin/cs
%_prefix/lib/mono/msbuild/15.0/bin/ko
%_prefix/lib/mono/msbuild/15.0/bin/de
%_prefix/lib/mono/msbuild/15.0/bin/en
%_prefix/lib/mono/msbuild/15.0/bin/es
%_prefix/lib/mono/msbuild/15.0/bin/it
%_prefix/lib/mono/msbuild/15.0/bin/pl
%_prefix/lib/mono/msbuild/15.0/bin/pt-BR
%_prefix/lib/mono/msbuild/15.0/bin/tr
%_prefix/lib/mono/msbuild/15.0/bin/zh-Hans
%_prefix/lib/mono/msbuild/15.0/bin/zh-Hant
%_prefix/lib/mono/msbuild/15.0/bin/Sdks
%_prefix/lib/mono/msbuild/15.0/bin/*.config
%_prefix/lib/mono/msbuild/15.0/bin/*.dll
%_prefix/lib/mono/msbuild/15.0/bin/*.overridetasks
%_prefix/lib/mono/msbuild/15.0/bin/*.pdb
%_prefix/lib/mono/msbuild/15.0/bin/*.props
%_prefix/lib/mono/msbuild/15.0/bin/*.rsp
%_prefix/lib/mono/msbuild/15.0/bin/*.targets
%_prefix/lib/mono/msbuild/15.0/bin/*.tasks
%_prefix/lib/mono/msbuild/15.0/bin/*.xml
%_prefix/lib/mono/msbuild/15.0/bin/*.xsd
%_prefix/lib/mono/xbuild/*
%_prefix/share/man/*/*
%_bindir/*

%files sdkresolver
%defattr(-,root,root)
%_prefix/lib/mono/msbuild/15.0/bin/SdkResolvers/*/*
