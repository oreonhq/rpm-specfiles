%global pypi_name pycotap

Name:           python-%{pypi_name}
Version:        1.3.1
Release:        11%{?dist}
Summary:        A tiny test runner that outputs TAP results to standard output

License:        MIT
URL:            https://github.com/remko/pycotap
Source0:        https://files.pythonhosted.org/packages/source/p/pycotap/pycotap-1.3.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 674355f01300be03df7f871784e498652c2d89ac19cd77ee8e61652634a2f83a
%global source0_file pycotap-1.3.1.tar.gz
# oreon url source checksums end
BuildArch:      noarch

BuildRequires:  python3-devel

%description
pycotap is a simple Python test runner for unit tests that outputs Test Anything
Protocol results directly to standard output. Contrary to other TAP runners
for Python, pycotap prints TAP (and *only* TAP) to standard output
instead of to a separate file, allowing you to pipe it directly to TAP pretty
printers and processors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
pycotap is a simple Python test runner for unit tests that outputs Test Anything
Protocol results directly to standard output. Contrary to other TAP runners
for Python, pycotap prints TAP (and *only* TAP) to standard output
instead of to a separate file, allowing you to pipe it directly to TAP pretty
printers and processors.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pycotap-1.3.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "674355f01300be03df7f871784e498652c2d89ac19cd77ee8e61652634a2f83a" || { echo "oreon: Source0 SHA256 mismatch for pycotap-1.3.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
find %{buildroot}/%{python3_sitelib} -name '*.py' | xargs sed -i '/^#!/d'
%__rm -f %{buildroot}/usr/COPYING

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-11
- Prepare for Oreon 11 (RP1)
