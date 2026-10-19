%global source0_hash e80f9c412db43f975640f09ec25a7bab8796a2fbf00005bff51eafacfc6549fb
%global pkg ansible-vault-mode
Name:           emacs-%{pkg}
Version:        0.6.1
Release:        1%{?dist}
Summary:        Minor mode for in place manipulation of ansible-vault
License:        GPL-3.0-or-later
URL:            https://github.com/freehck/%{pkg}
Source0:        https://github.com/freehck/%{pkg}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
Requires:       ansible-core
Requires:       emacs(bin)%{?_emacs_version: >= %{_emacs_version}}
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs-nw
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build

%{_emacs_bytecompile} ansible-vault.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 ansible-vault.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
