%global source0_hash 0908ae2af79a6549e7be1708745c09a101bbb6681fd41f492294e1d9dc77dfb6

Name:           python-beanprice
Version:        2.0.0
Release:        %autorelease
Summary:        Price quotes fetcher for Beancount

License:        GPL-2.0-only
URL:            https://github.com/beancount/beanprice
Source:         %{pypi_source beanprice}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides a script to fetch market data prices from various sources
on the Internet and render them for plain text accounting price syntax
(and Beancount).}

%description %_description

%package -n     beanprice
Summary:        %{summary}
Requires:       python3-beanprice = %{version}-%{release}

%description -n beanprice %_description

%package -n     python3-beanprice
Summary:        %{summary}

%description -n python3-beanprice %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n beanprice-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l beanprice

# Remove spurious directories
rm -r %{buildroot}%{python3_sitelib}/experiments/

%check
# coincap_test expects the system timezone to be UTC
TZ=UTC %pytest -v

%files -n beanprice
%doc README.md
%{_bindir}/bean-price

%files -n python3-beanprice -f %{pyproject_files}

%changelog
%autochangelog
