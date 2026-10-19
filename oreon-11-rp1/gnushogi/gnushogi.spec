%global source0_hash 3d3e4c0d7ce29cd0c18bcd2020a7330dd7d4b15b18b08ec493fffa13cc92a5f9
Name:           gnushogi
%global commit 5bb0b5b2f6953b3250e965c7ecaf108215751a74
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Version:        1.5
Release:        1%{?dist}
Summary:        Shogi, the Japanese version of chess
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gnushogi/
Source0:        https://git.savannah.gnu.org/cgit/%{name}.git/snapshot/%{name}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  texinfo-tex
# /oreon:deps
%description
GNU shogi is a program that plays shogi, the Japanese version of chess, 
against a human (or computer) opponent. It is only the AI engine, and you 
will likely want to use a GUI front-end (XBoard, for example) to be more 
comfortable.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{commit}
./autogen.sh

%build

%configure
%make_build
make -C gnushogi gnushogi.bbk
%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
cp gnushogi/gnushogi.bbk %{buildroot}%{_libdir}/%{name}
%oreon_autofiles main

%post

if [ -f /etc/xboard.conf ] ; then
    sed -i '/-firstChessProgramNames/a "GNUShogi" -fcp gnushogi -variant shogi' /etc/xboard.conf
fi
%preun

grep '\-fcp gnushogi \-variant shogi' /etc/xboard.conf > /dev/null 2>&1
if [ $? = 0 ] ; then
    sed -i '/-fcp gnushogi -variant shogi/d' /etc/xboard.conf
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
