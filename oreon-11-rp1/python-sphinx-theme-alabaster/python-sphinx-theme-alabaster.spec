Name:           python-sphinx-theme-alabaster
Version:        0.7.16
Release:        %autorelease -b 3
Summary:        Configurable sidebar-enabled Sphinx theme

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/alabaster
Source:         %{pypi_source alabaster}
# oreon url source checksums begin
%global source0_sha256 75a8b99c28a5dad50dd7f8ccdd447a121ddb3892da9e53d1ca5cca3106d58d65
%global source0_file alabaster-0.7.16.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

# Upstream lists no runtime dependencies,
# but alabaster/support.py imports from pygments.
# This is fine, as the module is only used for pygments.
# This BuildRequires is necessary for a successful import check.
BuildRequires:  python%{python3_pkgversion}-pygments

%global _description %{expand:
Alabaster is a visually (c)lean, responsive, configurable theme for the Sphinx
documentation system.

It began as a third-party theme, and is still maintained separately,
but as of Sphinx 1.3, Alabaster is an install-time dependency of Sphinx and is
selected as the default theme.}

%description %_description


%package -n     python%{python3_pkgversion}-sphinx-theme-alabaster
Summary:        %{summary}
%py_provides    python%{python3_pkgversion}-alabaster

%description -n python%{python3_pkgversion}-sphinx-theme-alabaster %_description


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/alabaster-0.7.16.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "75a8b99c28a5dad50dd7f8ccdd447a121ddb3892da9e53d1ca5cca3106d58d65" || { echo "oreon: Source0 SHA256 mismatch for alabaster-0.7.16.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n alabaster-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files alabaster


%check
# upstream has no tests
%pyproject_check_import


%files -n python%{python3_pkgversion}-sphinx-theme-alabaster -f %{pyproject_files}
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.16-1
- Prepare for Oreon 11 (RP1)
