%global source1_hash 054ee79eaa6124130202378f31b51b3a058a5e4cf6023dedcc0b1e345d2bdbae
%global source0_hash 6bef86a64020ba6eaf6a2d46552b56c60bffbbb31fd4a46ee16614a4b10c978b
%bcond check 0
%global watcher_name aw-awatcher
%global aw_server_rust_commit 656f3c97b3b5fb9be96b9e3a60f52c9e5cfdaf67
%global aw_server_rust_short_commit %(c=%{aw_server_rust_commit}; echo ${c:0:7})
Name:           awatcher
Version:        0.4.0
Release:        1%{?dist}
Summary:        A window activity and idle watcher
License:        Apache-2.0 AND BSL-1.0 AND BSD-3-Clause AND (Apache-2.0 WITH LLVM-exception) AND ISC AND MIT AND Unicode-DFS-2016 AND Unicode-3.0 AND MPL-2.0 AND Unlicense
URL:            https://github.com/2e3s/awatcher
Source0:        https://github.com/2e3s/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/ActivityWatch/aw-server-rust/archive/%{aw_server_rust_commit}/aw-server-rust-%{aw_server_rust_short_commit}.tar.gz
Patch0:         0001-Use-locally-downloaded-aw-server-rust.patch
Patch1:         0002-Fix-dependencies-to-the-one-used-in-Fedora.patch
Patch2:         0003-Remove-cosmic-watcher.patch
Patch3:         0004-Remove-unneeded-dev-dependencies.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  help2man
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{summary}.

%package     -n %{watcher_name}
Requires:       aw-server-rust
Summary:        A window activity and idle watcher
Provides:       bundled(aw-server-rust)
%description -n %{watcher_name}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -N
tar -xf %{SOURCE1} --strip-components 1 aw-server-rust-%{aw_server_rust_commit}/{aw-client-rust,aw-models}
%autopatch -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -Dm 0755 target/release/%{name} %{buildroot}%{_bindir}/%{watcher_name}
mkdir -p %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{watcher_name} -o %{buildroot}%{_mandir}/man1/%{watcher_name}.1
install -Dm 0644 config/%{watcher_name}.service -t %{buildroot}%{_userunitdir}
%oreon_autofiles aw-awatcher usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%post -n %{watcher_name}

%systemd_user_post %{watcher_name}.service
%preun -n %{watcher_name}

%systemd_user_preun %{watcher_name}.service
%postun -n %{watcher_name}

%systemd_user_postun_with_restart %{watcher_name}.service
%files -f %{oreon_filedir}/main.list
%files -n aw-awatcher -f %{oreon_filedir}/aw-awatcher.list

%changelog

%autochangelog
