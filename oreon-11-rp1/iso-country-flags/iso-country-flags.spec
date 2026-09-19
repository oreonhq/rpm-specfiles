%global source0_hash 46bda5a97adc470b831d29c449baacc5836357c6eb445cc2bb3567f771214b88

%global gitowner gosquared
%global gitproject flags
%global commit 1d382a9ea87667ac59c493b8fd771f49ce837e6a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		iso-country-flags
Version:	0
Release:	0.11.20170202git%{shortcommit}%{?dist}
License:	MIT
Summary:	Country flags
URL:		https://github.com/%{gitowner}/%{gitproject}
Source0:	https://github.com/%{gitowner}/%{gitproject}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:	noarch

%description
ISO 3166-1 alpha-2 defines two-letter country codes which are used most
prominently for the Internet's country code top-level domains.
This package contains 244 country flag PNG icons.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gitproject}-%{commit}
BASE="flags/flags-iso/flat"
# 1. rm extra dirs
rm -rf ${BASE}/{icns,ico}
# 2. rm extra flags
rm -rf ${BASE}/*/_*.png
# 3. filenames to lowercase
for i in `ls ${BASE}/*/*.png`; do mv $i `echo $i | tr [:upper:] [:lower:]`; done

%build
# nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r flags/flags-iso/flat/* %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE.txt
%doc README.md
%{_datadir}/%{name}/

%changelog
%autochangelog
