%global source0_hash 91337427a480e549f322d22697ec72a173b0e91eae2177e145cc7d9f4f967279
%bcond check 1
%global crate redlib
Name:           rust-redlib
Version:        0.35.1
Release:        1%{?dist}
Summary:        Alternative private front-end to Reddit
License:        AGPL-3.0-only
URL:            https://crates.io/crates/redlib
Source0:        https://static.crates.io/crates/redlib/redlib-%{version}.crate
Patch:          redlib-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Alternative private front-end to Reddit
License:        %{shrink:
    AGPL-3.0-only AND
    Apache-2.0 AND
    BSD-3-Clause AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Zlib AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
%post -n %{crate}

%systemd_post redlib.service
%preun -n %{crate}

%systemd_preun redlib.service
%postun -n %{crate}

%systemd_postun_with_restart redlib.service
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_sysconfdir} contrib/redlib.conf
install -Dpm0644 -t %{buildroot}%{_unitdir} contrib/redlib.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%{cargo_test -- -- --exact %{shrink:
    --skip client::test_localization_popular
    --skip client::test_obfuscated_share_link
    --skip client::test_share_link_strip_json
    --skip oauth::test_oauth_client
    --skip oauth::test_oauth_token_exists
    --skip subreddit::test_fetching_subreddit
    --skip user::test_fetching_user
    --skip utils::test_fetching_nsfw_subreddit
    --skip utils::test_fetching_subreddit_quarantined
    --skip utils::test_fetching_ws
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n redlib -f %{oreon_filedir}/redlib.list

%changelog

%autochangelog
