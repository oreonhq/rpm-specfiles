%global source0_hash 21ecf1fb5e7f8e70591faf5d2156e9439c59127aa2195de21617511fc3fe6d36

%global service rust2rpm

Name:           obs-service-%{service}
Version:        1
Release:        16%{?dist}
Summary:        OBS source service: Generate rpm packaging for Rust crates

License:        MIT
URL:            https://pagure.io/fedora-rust/%{name}
Source0:        https://releases.pagure.org/fedora-rust/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  rust-srpm-macros >= 9
Requires:       rust2rpm >= 9
Supplements:    ((obs-source_service or osc) and rust2rpm)

BuildArch:      noarch
ExclusiveArch:  %{rust_arches} noarch

%description
This is a source service for openSUSE Build Service.

This simply runs rust2rpm for a given Rust crate on crates.io
to generate RPM packaging to build packages for crates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# Nothing to build

%install
%make_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/rust2rpm*
%dir %{_localstatedir}/cache/obs
%dir %{_localstatedir}/cache/obs/rust2rpm

%changelog
%autochangelog
