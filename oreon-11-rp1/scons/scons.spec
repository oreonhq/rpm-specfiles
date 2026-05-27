%global source0_hash 99c0e94a42a2c1182fa6859b0be697953db07ba936ecc9817ae0d218ced20b15
%global source1_hash 26846230517c4b953edb444a3f22756f2b283eab1f3ecfb712de00f20478adf2

%global pypi_name scons

# Package documentation files
%bcond_without doc

# Install prebuilt documentation
%bcond_without prebuilt_doc

Name:      scons
Version:   4.10.1
Release:   %autorelease
Summary:   An Open Source software construction tool
# SCons/Tool/docbook/docbook-xsl-1.76.1/ are licensed under DocBook-Stylesheet
# MIT is main license
License:   MIT AND DocBook-Stylesheet
URL:       http://www.scons.org
Source0:        https://files.pythonhosted.org/packages/source/s/scons/scons-4.10.1.tar.gz
Source1:   https://scons.org/doc/production/scons-doc-%{version}.tar.gz

# Support python-setuptools < 79
Patch0:    scons-4.10.1-license_old_style.patch

BuildArch: noarch
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
BuildRequires: rst2pdf, fop, ghostscript
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%if 0%{with prebuilt_doc}
%autosetup -n scons-%{version} -N
%setup -n scons-%{version} -q -T -D -a 1
%else
%autosetup -n scons-%{version} -N -T -b 0
%endif

%if 0%{?fedora} < 43 || 0%{?rhel} > 9
%patch -P 0 -p1 -b .backup
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files SCons

rm -rfv %{buildroot}%{_bindir}/__pycache__
rm -rfv %{buildroot}%{python3_sitelib}/SCons/Tool/docbook/__pycache__

# Install manpages
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
%if 0%{without prebuilt_doc}
%doc build/doc/PDF build/doc/HTML build/doc/TEXT
%else
%doc PDF HTML EPUB TEXT
%endif
%license LICENSE
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.10.1-1
- Prepare for Oreon 11 (RP1)
