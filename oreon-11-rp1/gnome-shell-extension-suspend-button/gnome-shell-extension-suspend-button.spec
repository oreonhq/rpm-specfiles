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
Release:	20%{?gitrel}%{?dist}
Summary:	GNOME Shell Extension Suspend-Button by laserb

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://extensions.gnome.org/extension/826/suspend-button/
Source0:	%{giturl}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?gitversion}.tar.gz

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	%{_bindir}/glib-compile-schemas
BuildRequires: make

Requires:	gnome-shell-extension-common

%description
Allows to modify the suspend/shutdown button in the status menu.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p 1

%build
%make_build

%install
%make_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Install schema.
%{__mkdir} -p %{buildroot}%{gschemadir}
%{__cp} -pr _build/schemas/*gschema.xml %{buildroot}%{gschemadir}

# Install i18n.
%{_bindir}/find _build -name '*.po' -print -delete
%{__cp} -pr _build/locale %{buildroot}%{_datadir}

# Create manifest for i18n.
%find_lang %{name} --all-name

# Fedora handles this using triggers.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
	%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif

%files -f %{name}.lang
%license COPYING
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml

%changelog
%autochangelog
