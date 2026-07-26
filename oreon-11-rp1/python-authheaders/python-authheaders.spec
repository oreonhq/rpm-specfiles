%global source0_hash 118edc6d3cb1ad18ffab3d788ccc562fca2854cd645faab08fc47033c648148a

# Some tests fail. Pass --with all_tests to retry
%bcond_with all_tests

# Created by pyp2rpm-3.3.4
%global pypi_name authheaders

Name:           python-%{pypi_name}
Version:        0.16.3
Release:        7%{?dist}
Summary:        A library wrapping email authentication header verification and generation

# Licensing described in LICENSE file
License:        MIT and ZPL-2.1
URL:            https://github.com/ValiMail/authentication-headers
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  help2man

%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       publicsuffix-list

%description -n python3-%{pypi_name}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled publicsuffix data
rm -f %{pypi_name}/public_suffix_list.txt
# Use public suffix data from installed RPM
ln -s %{_datadir}/publicsuffix/public_suffix_list.dat %{pypi_name}/public_suffix_list.txt
# fix shebang
sed -i '/^#!\/usr\/bin\/python3/,+2 d' %{pypi_name}/dmarcpolicyfind.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} help2man --no-info \
  --name="Find DMARC policy for a domain" \
  --version-string=%{version} \
  %{buildroot}%{_bindir}/dmarc-policy-find \
  -o %{buildroot}%{_mandir}/man1/dmarc-policy-find.1

%check
%pyproject_check_import %{pypi_name}
# test_authenticate_dmarc_psdsub: test fixture not shipped
%pytest -v \
%if %{without all_tests}
  -k "not test_authenticate_dmarc_psdsub" \
%endif
;

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGES
%license COPYING
%{_bindir}/dmarc-policy-find
%{_mandir}/man1/dmarc-policy-find.1*

%changelog
%autochangelog
