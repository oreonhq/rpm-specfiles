%global source0_hash c2f259e683baed02399023d1f68442aebf46f7330aa5d76fab6f2766d6d8a7dc

Name:           showcert
Version:        0.4.12
Release:        1%{?dist}
Summary:        inspect TLS certificates presented by remote servers

License:        MIT
URL:            https://github.com/yaroslaff/showcert
Source:         %{pypi_source showcert}

Patch1:         showcert-remove-dependency-on-python-magic.patch

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  (python3dist(magic) or python3dist(file-magic))
Requires:       (python3dist(magic) or python3dist(file-magic))

%description
Simple OpenSSL for humans: all you need for X.509 TLS certificates (and
nothing more).

showcert consist of two CLI utilities: showcert itself - all 'read' operations
with X.509 certificates and gencert - to create certificates for development
purposes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n showcert-%{version}
%py3_shebang_fix showcert/cli/*.py
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l showcert

%check
# upstream tests run against a couple of well-known sites, no tests
# for code so just try to run some superficial smoke tests:
%pyproject_check_import

export PATH=%{buildroot}%{_bindir}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
showcert --help
gencert --help

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/showcert
%{_bindir}/gencert

%changelog
%autochangelog
