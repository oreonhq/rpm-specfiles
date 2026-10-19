%global source0_hash 9bbfbea3a5ee2ca83594f12be59d45df59dd5a7ee3c6383129ef6f033bb65a1c
%bcond check 1
%global cargo_install_lib 0
Name:           ripgrep-edit
Version:        0.3.8
Release:        1%{?dist}
Summary:        Edit ripgrep search results across multiple files
License:        %{shrink:
    (GPL-3.0-or-later OR AGPL-3.0-or-later) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    MIT
}
URL:            https://gitlab.com/aarcange/ripgrep-edit
Source0:        https://gitlab.com/aarcange/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Requires: ripgrep
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  emacs-nw
BuildRequires:  ripgrep
BuildRequires:  rustc
# /oreon:deps
%description
Edit ripgrep search results across multiple files.

%package        emacs
BuildRequires:  emacs-nw
BuildArch:      noarch
Requires:       emacs-filesystem >= %{_emacs_version}
Requires:       %{name} = %{version}-%{release}
Summary:        Use Emacs to edit ripgrep search results across multiple files
%description emacs
Use Emacs to edit ripgrep search results across multiple files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n ripgrep-edit-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -Dpm 0755 target/rpm/rg-edit -t %{buildroot}%{_bindir}
install -m0644 -D emacs/rg-edit.el %{buildroot}%{_emacs_sitestartdir}/rg-edit-init.el
install -m0644 -D -t %{buildroot}%{_mandir}/man1/ target/rpm/build/%{name}-*/man/*.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ripgrep-edit-emacs -f %{oreon_filedir}/ripgrep-edit-emacs.list

%changelog

%autochangelog
