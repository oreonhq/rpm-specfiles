%global source0_hash c0124c5a03d0ec6066ca329884b2cdd75fea84eaf64f4e5fc5d59b111a43afa3
%global pkg lua
%global commit 2d9a468b94acd8480299d47449b53136060b7b23
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		emacs-lua
Version:	20210802
Release:        1%{?dist}
Summary:        Lua major mode for GNU Emacs
License:	GPL-2.0-or-later
URL:		http://immerrr.github.com/lua-mode
Source0:        https://github.com/immerrr/%{pkg}-mode/archive/%{commit}/%{pkg}-mode-%{shortcommit}.tar.gz
Source1:	lua-init.el
BuildArch:	noarch
Requires:	emacs(bin) >= 24.3
# oreon:deps
BuildRequires:  emacs
BuildRequires:  pkgconfig
# /oreon:deps
%description
A GNU Emacs major mode for editing Lua code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lua-mode-%{commit}

%build

%{_emacs_bytecompile} lua-mode.el
%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{pkg}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 lua-mode.el %{buildroot}%{_emacs_sitelispdir}/%{pkg}
install -p -m 0644 lua-mode.elc %{buildroot}%{_emacs_sitelispdir}/%{pkg}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
