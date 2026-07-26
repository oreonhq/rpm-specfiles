%global source0_hash c0124c5a03d0ec6066ca329884b2cdd75fea84eaf64f4e5fc5d59b111a43afa3

%global pkg lua
%global commit 2d9a468b94acd8480299d47449b53136060b7b23
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		emacs-lua
Version:	20201010
Release:	13.20210121git2d9a468%{?dist}
Summary:	Lua major mode for GNU Emacs

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://immerrr.github.com/lua-mode
Source0:	https://github.com/immerrr/lua-mode/archive/%{commit}/lua-mode-%{shortcommit}.tar.gz
Source1:	lua-init.el
BuildArch:	noarch

BuildRequires:	emacs >= 24.3
BuildRequires:	pkgconfig
Requires:	emacs(bin) >= 24.3

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

%files
%license COPYING
%doc NEWS README.md
%{_emacs_sitelispdir}/%{pkg}
%{_emacs_sitestartdir}/lua-init.el

%changelog
%autochangelog
