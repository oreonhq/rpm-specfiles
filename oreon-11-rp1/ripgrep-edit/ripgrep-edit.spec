%global source0_hash 9bbfbea3a5ee2ca83594f12be59d45df59dd5a7ee3c6383129ef6f033bb65a1c

%bcond check 1

# prevent library files from being installed
%global cargo_install_lib 0

Name:           ripgrep-edit
Version:        0.3.8
Release:        %autorelease
Summary:        Edit ripgrep search results across multiple files

# https://docs.fedoraproject.org/en-US/legal/license-field/ discourages the use of SourceLicense
# SourceLicense:  GPL-3.0-or-later OR AGPL-3.0-or-later
License:        %{shrink:
    (GPL-3.0-or-later OR AGPL-3.0-or-later) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    MIT
}
URL:            https://gitlab.com/aarcange/ripgrep-edit
Source:         https://gitlab.com/aarcange/ripgrep-edit/-/archive/%version/%name-%version.tar.gz

BuildRequires:  cargo-rpm-macros ripgrep
Requires: ripgrep

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
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dpm 0755 target/rpm/rg-edit -t %{buildroot}%{_bindir}
install -m0644 -D emacs/rg-edit.el %{buildroot}%{_emacs_sitestartdir}/rg-edit-init.el
install -m0644 -D -t %{buildroot}%{_mandir}/man1/ target/rpm/build/%{name}-*/man/*.1

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE.dependencies
%doc README.md
%{_bindir}/rg-edit
%{_mandir}/man1/rg-edit.1*

%files emacs
%{_emacs_sitestartdir}/rg-edit-init.el

%changelog
%autochangelog
