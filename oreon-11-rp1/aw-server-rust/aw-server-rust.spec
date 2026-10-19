%global source0_hash 7e4e0d61f3eecd272f4f7a2985f9204327e554d126d721f4db70e8e20a106474
%bcond check 1
%global commit 9a8802a374d8e9f587b343dfedf3859ec1a9bba2
%global short_commit %(c=%{commit}; echo ${c:0:7})
Name:           aw-server-rust
Version:        0.13.1^20260309.git%{short_commit}
Release:        1%{?dist}
Summary:        A re-implementation of aw-server in Rust
License:        MPL-2.0 AND Apache-2.0 AND BSD-3-Clause AND MIT AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT) AND Unicode-3.0 AND Zlib
URL:            https://github.com/ActivityWatch/aw-server-rust
Source0:        https://github.com/ActivityWatch/%{name}/archive/%{commit}/%{name}-%{short_commit}.tar.gz
Patch0:         0001-Remove-vendored-openssl.patch
Patch1:         0002-Remove-Android-dependencies.patch
Patch2:         0003-Remove-jemallocator.patch
Patch3:         0004-Fix-fancy-regex-dependency-to-the-one-used-in-Fedora.patch
Patch4:         0005-Fix-rusqlite-dependency-to-the-one-used-in-Fedora.patch
Patch5:         0006-Remove-criterion.patch
Patch6:         0007-Allow-dirs-6.patch
Patch7:         0008-Allow-fancy-regex-versions-through-0.17.patch
ExcludeArch:     ppc64le
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  help2man
BuildRequires:  nodejs-aw-webui
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{summary}

%package     -n aw-sync-rust
Summary:        A re-implementation of aw-server in Rust
Requires:       %{name} = %{version}-%{release}
%description -n aw-sync-rust
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{commit} -p1
sed -ri 's/version = ("[[:alnum:]]+\.[[:alnum:]]+\.[[:alnum:]]+)/version = \1+%{short_commit}/' aw-server/Cargo.toml
%oreon_vendor_cargo
%build

export AW_WEBUI_DIR="%{_datadir}/aw-webui/dist/"
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -Dm 0755 target/rpm/{aw-server,aw-sync} -t %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/aw-server -o %{buildroot}%{_mandir}/man1/aw-server.1
help2man %{buildroot}%{_bindir}/aw-sync -o %{buildroot}%{_mandir}/man1/aw-sync.1
install -Dm 0644 aw-server.service -t %{buildroot}%{_userunitdir}
%oreon_autofiles aw-sync-rust usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export AW_WEBUI_DIR="%{_datadir}/aw-webui/dist/"
%cargo_test
%endif
%post

%systemd_user_post aw-server.service
%preun

%systemd_user_preun aw-server.service
%postun

%systemd_user_postun_with_restart aw-server.service
%files -f %{oreon_filedir}/main.list
%files -n aw-sync-rust -f %{oreon_filedir}/aw-sync-rust.list

%changelog

%autochangelog
