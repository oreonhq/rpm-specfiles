# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4210d1a80a62e986029208117991b6347ccaaaab37b67463a3ff31ee065dc487
%global source1_hash 5a9d2b5a6b64e23c748e2735d0c59cc2b28b6f5f7e8ec61d12d3406051e6cb1f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pypi_name scons

%bcond_without doc

%bcond_without prebuilt_doc

Name:      scons
Version:   4.11.1
Release:        %{autorelease}
Summary:   An Open Source software construction tool
License:   MIT AND DocBook-Stylesheet
URL:       http://www.scons.org
Source0:   %{pypi_source}
Source1:   https://scons.org/doc/production/scons-doc-%{version}.tar.gz
Patch0:    scons-4.11.0-license_old_style.patch
BuildArch: noarch
BuildRequires: oreon-rpm-macros
BuildRequires: make
%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%if %{with doc}
%package doc
Summary: An Open Source software construction tool
BuildArch: noarch
%if 0%{without prebuilt_doc}
BuildRequires: python3-sphinx >= 5.1.1
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: rst2pdf
BuildRequires: fop
BuildRequires: ghostscript
BuildRequires: python3dist(readme-renderer)
%endif
%description doc
Scons documentation.
%endif

%package -n     python3-%{name}
Summary: An Open Source software construction tool
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
%py_provides    scons-python3
%py_provides    python3-%{name}
%py_provides    SCons
%py_provides    scons
%description -n python3-%{name}
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.
SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%if 0%{with prebuilt_doc}
%autosetup -n scons-%{version} -N
%setup -n scons-%{version} -q -T -D -a 1
%else
%autosetup -n scons-%{version} -N -T -b 0
%endif

%if 0%{?fedora} < 43 || 0%{?rhel} > 9
%patch -P 0 -p1 -b .backup
%endif

rm -rf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files SCons

rm -rfv %{buildroot}%{_bindir}/__pycache__
rm -rfv %{buildroot}%{python3_sitelib}/SCons/Tool/docbook/__pycache__

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 *.1 %{buildroot}%{_mandir}/man1/
rm -f %{buildroot}%{_prefix}/*.1

%files -n python3-%{name} -f %{pyproject_files}
%if 0%{?fedora} < 43 || 0%{?rhel} > 9
%license LICENSE SCons/Tool/docbook/docbook-xsl-1.76.1/COPYING
%endif
%{_bindir}/%{name}
%{_bindir}/%{name}ign
%{_bindir}/%{name}-configure-cache
%{_mandir}/man1/*

%if %{with doc}
%files doc
%if %{without prebuilt_doc}
%doc build/doc/PDF build/doc/HTML build/doc/TEXT
%else
%doc PDF HTML EPUB TEXT
%endif
%license LICENSE
%endif

%changelog
%autochangelog
