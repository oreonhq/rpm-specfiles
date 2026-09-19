%global source0_hash 56d35f02dc4c8dd386a7242007432adc458466c8a48d0d680eda1826197ca17b

%global pkg color-theme
%global pkgname Emacs Color Themes

Name:		emacs-%{pkg}
Version:	6.6.0
Release:	33%{?dist}
Summary:	Color themes for Emacs

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.nongnu.org/color-theme
Source0:	http://ftp.twaren.net/Unix/NonGNU/color-theme/%{pkg}-%{version}.tar.gz
Source1:	emacs-color-theme-init.el
#Patches are submitted to upstream
#http://lists.nongnu.org/archive/html/color-theme-devel/2010-04/msg00000.html
#Patch to fix Makefile
Patch0:		emacs-%{pkg}-fix-compile.patch
#Patch to fix README
Patch1:		emacs-%{pkg}-fix-readme.patch
#Patch to fix License file
Patch2:		emacs-%{pkg}-fix-copying-eol.patch

BuildArch:	noarch
BuildRequires:	emacs
BuildRequires: make
Requires:	emacs(bin) >= %{_emacs_version}

Obsoletes:      %{name}-el < 6.6.0-28
Provides:       %{name}-el = %{version}-%{release}

%description
%{pkgname} is an add-on package for GNU Emacs.
It provides a lot of different color themes to skin your Emacs greatly
improving the editing experience. It also includes a neat framework to
help you creating new themes from your current emacs customization's.
Also features an easy way to share your custom themes with the world.  

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkg}-%{version}
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{pkg}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{pkg}/themes
mkdir -p %{buildroot}%{_emacs_sitestartdir}/
cp %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/
cp *.el *.elc %{buildroot}%{_emacs_sitelispdir}/%{pkg}
cp themes/*.el themes/*.elc %{buildroot}%{_emacs_sitelispdir}/%{pkg}/themes

%files
%doc COPYING README
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitelispdir}/%{pkg}/themes/*.el
%{_emacs_sitelispdir}/%{pkg}/themes/*.elc
%dir %{_emacs_sitelispdir}/%{pkg}
%{_emacs_sitestartdir}/emacs-color-theme-init.el

%changelog
%autochangelog
