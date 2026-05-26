%global srcname httplib2

Name:           python-%{srcname}
Version:        0.22.0
Release:        8%{?dist}
Summary:        Comprehensive HTTP client library
License:        MIT
URL:            https://pypi.python.org/pypi/httplib2
Source:         https://github.com/httplib2/httplib2/archive/v%{version}/%{srcname}-%{version}.tar.gz
#
# Patch to use the Fedora ca certs instead of the bundled ones
#
Patch1:         python-%{srcname}.certfile.patch
# oreon url source checksums begin
%global source0_sha256 f0463bc04d2546325eaba1da15f8e45763ed2a52b47c0331c721f1c85470c9ca
%global source0_file httplib2-0.22.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch

%global _description\
A comprehensive HTTP client library that supports many features left out of\
other HTTP libraries.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-pytest
# This is listed as a test requirement, but doesn't seem to actually be used.
#BuildRequires:  python3-pytest-forked
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-six
BuildRequires:  python3-cryptography
# This is a runtime dependency required to run the tests:
BuildRequires:  python3-pyparsing

%description -n python3-%{srcname} %{_description}


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/httplib2-0.22.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f0463bc04d2546325eaba1da15f8e45763ed2a52b47c0331c721f1c85470c9ca" || { echo "oreon: Source0 SHA256 mismatch for httplib2-0.22.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{srcname}-%{version}

# Drop coverage
sed -i '/--cov/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l httplib2

%check
# test_get_301_no_redirect is disabled because it leads to Segfault on Python 3.11
# the other disabled tests are broken PySocks tests
%pytest -k "not test_unknown_server \
	and not test_socks5_auth and not \
	test_server_not_found_error_is_raised_for_invalid_hostname and not \
	test_functional_noproxy_star_https and not \
	test_sni_set_servername_callback and not test_not_trusted_ca and not \
	test_invalid_ca_certs_path and not test_max_tls_version and not \
	test_get_301_via_https and not test_client_cert_password_verified and not\
	test_get_via_https and not test_min_tls_version and not\
	test_client_cert_verified and not test_inject_space and not test_get_301_no_redirect"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.22.0-8
- Prepare for Oreon 11 (RP1)
