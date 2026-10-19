%global source0_hash f12a31f8fc1e7a35e100ad818087158194d5740b2e03787bf8bea646a758c1f2
%global	repoid		54457
%global	minver_saphire	3.6.5
Name:		mfiler3
Version:	4.4.9
Release:        1%{?dist}
Summary:        Two pane file manager under UNIX console
License:	MIT
URL:		http://www.geocities.jp/daisuke530221jp/index3.html
Source0:        http://dl.sourceforge.jp/%{name}/%{repoid}/%{name}-%{version}.tgz
Source10:	mfiler3.sh
Obsoletes:	%{name}-mdnd < 3.0.0
Requires:	saphire >= %{minver_saphire}
# oreon:deps
BuildRequires:  cmigemo-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  oniguruma-devel
BuildRequires:  saphire-devel
# /oreon:deps
%description
Minnu's Filer3 is a two pane file manager under UNIX console.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Don't strip, preserve timestamp
%{__sed} -i.strip -e 's| -s -m| -m|' Makefile.in
%{__sed} -i.stamp -e 's|\([ \t][ \t]*install \)|\1 -p |' Makefile.in

# May have to ask the upstream...
%{__sed} -i.sao -e 's|saphire -c|saphire -rn -c|' Makefile.in

%{__rm} -f *.o

# Prefer less over lv
sed -i.pager \
	-e 's| lv| less|' \
	-e 's|lv |less |' \
	mfiler3.sa

%build

%configure \
	CC="gcc %{optflags} -D_XOPEN_SOURCE=700 -D_DEFAULT_SOURCE" \
	--sysconfdir=%{_libdir}/%{name} \
	--bindir=%{_libexecdir}/%{name} \
	--with-migemo \
	--with-system-migemodir=%{_datadir}/cmigemo
%{__make} -k \
	docdir=%{_defaultdocdir}/%{name}/
%install
rm -rf ./Trash
%makeinstall \
	sysconfdir=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	bindir=$RPM_BUILD_ROOT%{_libexecdir}/%{name} \
	docdir=$(pwd)/Trash/
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__install} -cpm 0755 %SOURCE10 $RPM_BUILD_ROOT%{_bindir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
