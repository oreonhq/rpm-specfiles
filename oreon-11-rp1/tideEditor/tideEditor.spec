%global source0_hash 45b1d545ab71676ee781488b309a61ab187137a66fe4b522faa103afd7ea0593

%global		postver	-r2
%global		postrpmver	%(echo "%postver" | sed -e 's|-|.|g' | sed -e 's|^\.||')

%global		mainver		1.5

%global		baserelease	12
%global		rpmrel		%{baserelease}%{?postver:.%postrpmver}

Name:		tideEditor
Version:	%{mainver}
Release:	%{rpmrel}%{?dist}
Summary:	Editor for Tide Constituent Database (TCD) files

# SPDX confirmed
License:	GPL-3.0-or-later
URL:		http://www.flaterco.com/xtide/
Source0:	ftp://ftp.flaterco.com/xtide/tideeditor-%{version}%{?postver}.tar.xz

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	qt4-devel
BuildRequires:	libtcd-devel
# Temporally
BuildRequires:	automake
Requires:	xtide-common

%description
tideEditor is an editor for Tide Constituent Database (TCD) files.  It
was written by Jan C. Depner but is now jointly maintained by David
Flater and Jan Depner.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n tideeditor-%{version}

sed -i.moc Makefile.in \
	-e '\@MOC@s|CPPFLAGS|CPPFLAGS_UNUSED|'

%build
export CPPFLAGS="$RPM_OPT_FLAGS"
for mod in \
	QtCore \
	QtGui \
	%{nil}
do
	export CPPFLAGS="${CPPFLAGS} $(pkg-config --cflags $mod)"
done	
export ac_cv_path_MOC=%{_bindir}/moc-qt4

%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS
%doc ChangeLog
%doc README
%license COPYING
%{_bindir}/tideEditor

%changelog
%autochangelog
