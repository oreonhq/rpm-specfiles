%global source0_hash 560440defe4f20ac22ce65e873c7ff60ca0c08318524afe6dae86adc4b13d714

Name:           vcsh
Version:        2.0.8
Release:        6%{?dist}
Summary:        Version Control System for $HOME

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/RichiH/%{name}
Source0:        https://github.com/RichiH/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildArch:      noarch
Requires:       git

BuildRequires:  git
BuildRequires:  make

%description
vcsh allows you to have several git repositories, all maintaining their working
trees in $HOME without clobbering each other. That, in turn, means you can have
one repository per config set (zsh, vim, ssh, etc), picking and choosing which
configs you want to use on which machine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%{make_install} DOCDIR=%{_pkgdocdir} ZSHDIR=%{_datadir}/zsh/site-functions

%files
%{_bindir}/%{name}
%{_mandir}/man*/%{name}*
%{_datadir}/bash-completion/
%{_datadir}/zsh/
%{_docdir}/%{name}
%{_defaultlicensedir}/%{name}

%changelog
%autochangelog
