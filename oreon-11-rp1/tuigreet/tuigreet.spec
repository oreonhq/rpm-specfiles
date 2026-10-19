%global source0_hash 7d643ba224c40c6a63f9462a826630543071aea08e732ccd2e880bcd80d939e8
Name:           tuigreet
Version:        0.11.1
Release:        1%{?dist}
Summary:        Graphical console greeter for greetd
License:        GPL-3.0-only AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND Unicode-3.0 AND Unicode-DFS-2016 AND (Unlicense OR MIT)
URL:            https://github.com/apognu/%{name}
Source0:        https://github.com/apognu/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          tuigreet-fix-metadata.diff
Patch:          tuigreet-0.9.1-Store-persistent-data-in-the-greetd-user-home.patch
Patch:          tuigreet-0.9.1-adjust-for-i18n-embed-0.16.patch
Requires:       greetd >= 0.6
Provides:       greetd-greeter = 0.6
Provides:       greetd-%{name} = %{version}
Obsoletes:      greetd-%{name} <= 0.8.0-1
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  scdoc
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
scdoc <contrib/man/tuigreet-1.scd >contrib/man/tuigreet.1
%install
%cargo_install
install -D -m644 -vp contrib/man/tuigreet.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
