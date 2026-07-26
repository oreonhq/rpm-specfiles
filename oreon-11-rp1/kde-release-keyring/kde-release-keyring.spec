%global source0_hash af8dff782b5cbad1fd6e1bdb9e4d05c9bfc02e465db57ff53aa8634ae8fd40da

%global commit ae8f4d5374f53cd07f965b53b1cf3f9b3254194c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250403
%global base_name release-keyring

Name:    kde-release-keyring
Version: 0~git%{commitdate}.%{shortcommit}
Release: 8%{?dist}
Summary: Keyring of signing keys from KDE community members

License: CC0-1.0
URL:     https://invent.kde.org/sysadmin/%{base_name}/
Source0: %{url}/-/archive/%{commit}/%{base_name}-%{shortcommit}.tar.gz

BuildArch:     noarch
BuildRequires: gnupg2

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{commit} -p1

%build
gpg --options /dev/null --no-default-keyring --keyring ./%{base_name}.kbx --import ./keys/*.asc

%install
install -m644 -p -D %{base_name}.kbx %{buildroot}%{_datadir}/%{name}/%{base_name}.kbx
install -d %{buildroot}%{_datadir}/%{name}/keys
install -m644 -p -D keys/* %{buildroot}%{_datadir}/%{name}/keys

%files
%license LICENSES/CC0-1.0.txt
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/keys/
%{_datadir}/%{name}/%{base_name}.kbx
%{_datadir}/%{name}/keys/*.asc

%changelog
%autochangelog
