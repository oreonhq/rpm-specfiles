%global source0_hash 839be1b26021f3a6e30db7fdc6eedfd1af03dee22ade56d028fde77433a807a3
%global pkg ddskk
%global pkgname Daredevil SKK
%global codename Neppu
Summary:        Daredevil SKK - Simple Kana to Kanji conversion program for Emacs
Name: emacs-common-ddskk
Version: 17.2_Mena
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://openlab.ring.gr.jp/skk/main.html
Source0:        https://github.com/skk-dev/%{pkg}/archive/refs/tags/%{pkg}-%{version}_%{codename}.tar.gz
Source1: ddskk-init.el
BuildArch: noarch
Requires(post): info
Requires(preun): info
# oreon:deps
BuildRequires:  emacs
BuildRequires:  make
# /oreon:deps
%description
Daredevil SKK is a branch of SKK (Simple Kana to Kanji conversion program,
an input method of Japanese). It forked from the maintrunk, SKK version 10.56.
It consists of a simple core and many optional programs which provide extensive
features, however, our target is to more simplify core, and more expand its
optional features.

This package does not include dictionaries or a skkserver. Please install them
separately.

%package -n emacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under GNU Emacs
Requires:	emacs(bin) >= %{_emacs_version}
Requires:	emacs-common-%{pkg} = %{version}-%{release}
Provides:	ddskk = %{version}-%{release}
Obsoletes:	ddskk < %{version}-%{release}
Provides:	emacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	emacs-%{pkg}-el < %{version}-%{release}
%description -n emacs-%{pkg}
This package contains the byte compiled elisp packages to run %{pkgname}
with GNU Emacs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{pkg}-%{version}_%{codename}

# We can't set SKK-MK-texinfo-coding-system in SKK-CFG since it is
# defined with defconst.

sed -ie "s!\(SKK-MK-texinfo-coding-system\) 'iso-2022-jp!\1 'utf-8!" SKK-MK

# We don't need information about other platforms
rm READMEs/README.MacOSX.ja
rm READMEs/README.w32.ja.org

# avoid buildroot in tutorial path
sed -ie "s!@TUT@!%{_datadir}/skk/SKK.tut!" skk-setup.el.in

%build

%install
mkdir -p %{buildroot}%{_datadir}/info
cat >> SKK-CFG <<EOF
(setq PREFIX "%{buildroot}%{_prefix}")
(setq SKK_LISPDIR "%{buildroot}%{_emacs_sitelispdir}/ddskk")
EOF
make EMACS=emacs install
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}
rm -f %{buildroot}%{_infodir}/dir
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n emacs-ddskk -f %{oreon_filedir}/emacs-ddskk.list

%changelog

%autochangelog
