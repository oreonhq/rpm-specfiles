%global source0_hash 447214df03a13931b46ba0216324c66a8bdbab845c14f2cbcd21e43e41a52a42

Name:           six
Version:        0.5.3
Release:        47%{?dist}
Summary:        Hex playing program

License:        GPL-1.0-or-later
URL:            http://six.retes.hu/
Source0:        http://six.retes.hu/download/%{name}-%{version}.tar.gz
Patch0:         six-gcc43.patch
Patch50:	six-fix-DSO.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  kdelibs3-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Six is a Hex  playing program for Linux/Un*x systems running KDE. It has a
strong AI, an easy to use GUI and can import emails from Richard's PBEM server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P50 -p0
%{__sed} -i 's/DocPath\=six\/six\.html/Categories\=Game\;BoardGame\;/' six/six.desktop
%{__sed} -i 's/Terminal\=0/Terminal\=false/' six/six.desktop
echo "Encoding=UTF-8" >> six/six.desktop

%build
%configure --disable-dependency-tracking
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/six/common

%find_lang %{name}

desktop-file-install                                    \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        --delete-original                               \
        $RPM_BUILD_ROOT%{_datadir}/applnk/Games/Board/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO VERSION
%{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/doc/HTML/en/%{name}
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/locolor
%{_datadir}/mimelnk/application/vnd.kde.six.desktop
%{_datadir}/applications/%{name}.desktop

%post
touch --no-create %{_datadir}/icons/locolor || :
%{_bindir}/gtk-update-icon-cache --quiet --ignore-theme-index %{_datadir}/icons/locolor || :

%postun
touch --no-create %{_datadir}/icons/locolor || :
%{_bindir}/gtk-update-icon-cache --quiet --ignore-theme-index %{_datadir}/icons/locolor || :

%changelog
%autochangelog
