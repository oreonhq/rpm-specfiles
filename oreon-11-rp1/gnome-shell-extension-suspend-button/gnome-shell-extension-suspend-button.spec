%global source0_hash ad147c2284098a34cc92aa26bf0cda0133801a5a7c6415f52ab5ad0897cad1de
%global extdir		%{_datadir}/gnome-shell/extensions/suspend-button@laserb
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global giturl		https://github.com/laserb/%{name}
%global commit		a81252074de99e2cdd29913b7f797a7f0d6d5b2b
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global commitdate	20171024
%global gitrel		.%{commitdate}git%{shortcommit}
%global gitver		-%{commitdate}git%{shortcommit}
Name:		gnome-shell-extension-suspend-button
Version:	19
Release:        1%{?dist}
Summary:        GNOME Shell Extension Suspend-Button by laserb
License:	GPL-2.0-or-later
URL:		https://extensions.gnome.org/extension/826/suspend-button/
Source0:        %{giturl}/archive/%{commit}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	gnome-shell-extension-common
# oreon:deps
BuildRequires:  /usr/bin/glib-compile-schemas
BuildRequires:  gettext
BuildRequires:  make
# /oreon:deps
%description
Allows to modify the suspend/shutdown button in the status menu.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p 1

%build

%make_build
%install
%make_install
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}
%{__mkdir} -p %{buildroot}%{gschemadir}
%{__cp} -pr _build/schemas/*gschema.xml %{buildroot}%{gschemadir}
%{_bindir}/find _build -name '*.po' -print -delete
%{__cp} -pr _build/locale %{buildroot}%{_datadir}
%find_lang %{name} --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
