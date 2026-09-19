%global source0_hash 1a257adabdc926be0db18af767e3a902fc6b1be37627a06b66714866bb6027a5

Name:		bltk
Version:	1.1.0
Release:	37%{?dist}
Summary:	The BLTK measures notebook battery life under any workload

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:			http://www.lesswatts.org/projects/bltk/
Source0:	http://www.lesswatts.org/patches/bltk/%{name}-%{version}.tar.gz
Source1:	bltk.conf
Source2:  OOCALC_FILE_SAMPLE.ods
Source3:  OODRAW_FILE_SAMPLE.odg
Source4:  OOWRITER_FILE_SAMPLE.odt

Patch1:  bltk-1.0.9-man.patch
Patch3:  bltk-1.0.9-bltk_paths.patch
Patch4:  bltk-1.0.9-opt_developer.patch
Patch5:  bltk-1.1.0-cond_install.patch
Patch6:  bltk-1.0.9-opt_game.patch
Patch7:  bltk-1.0.9-conf.patch
Patch8:  bltk-1.0.9-opt_office.patch
Patch10: bltk-1.0.9-opt_player.patch
Patch11: bltk-1.0.9-home_dir.patch
Patch12: bltk-1.0.9-opt_reader.patch
Patch13: bltk-1.0.9-installed.patch
Patch15: bltk-1.0.9-xse.patch
Patch16: bltk-1.0.9-conf_home.patch
Patch17: bltk-1.1.0-rm_sudo.patch
Patch18: bltk-1.0.9-plot-path.patch
Patch19: bltk-1.0.9-rpm.patch
Patch20: bltk-1.1.0-cflags-override.patch
Patch21: bltk-c99.patch

BuildRequires:	gcc, libX11-devel
BuildRequires: make

Requires: udisks2, gnuplot

%description
This tool kit is used to measure battery life and performance under
different workloads on Linux. Test can be used with various workloads to
simulate different types of laptop usage.
The following workloads are currently implemented:
	a) Idle workload - collect statistics only
	b) Developer workload - simulates code development in Linux environment
	c) Reader workload - simulates text reading on laptop
	d) DVD playback workload - simulates laptop entertaining usage
	e) 3d game workload - simulates 3D-gaming on laptop
	f) Office Activity workload - simulates laptop usage for different
		office activities (based on OpenOffice.org office suit)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n bltk

# %patch0 -p1 -b .all
%patch -P1 -p1 -b .man
%patch -P3 -p1 -b .bltk_paths
%patch -P4 -p1 -b .opt_developer
%patch -P5 -p1 -b .cond_install
%patch -P6 -p1 -b .opt_game
%patch -P7 -p1 -b .conf
%patch -P8 -p1 -b .opt_office
%patch -P10 -p1 -b .opt_player
%patch -P11 -p1 -b .home_dir
%patch -P12 -p1 -b .opt_reader
%patch -P13 -p1 -b .installed
%patch -P15 -p1 -b .xse
%patch -P16 -p1 -b .conf_home
%patch -P17 -p1 -b .rm_sudo
%patch -P18 -p1 -b .plot-path
%patch -P19 -p1 -b .rpm
%patch -P20 -p1 -b .cflags-override
%patch -P21 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"
#make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT PACKAGE_BUILD=y

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bltk
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bltk/{bin,lib,doc,wl_developer,wl_game,wl_office,wl_player,wl_reader}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_developer/bin
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_game/bin
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office/bin
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_player/bin
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_reader/bin
mkdir -p ${RPM_BUILD_ROOT}/etc
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,5}

install -m 644 %{SOURCE1}	${RPM_BUILD_ROOT}/etc
install -m 644 doc/bltk.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1
install -m 644 doc/bltk_report.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1
install -m 644 doc/bltk.conf.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5

install -m 755 bin/bat_drain	${RPM_BUILD_ROOT}%{_libdir}/bltk/bin/bat_drain
install -m 755 bin/bat_drain_table	${RPM_BUILD_ROOT}%{_libdir}/bltk/bin/bat_drain_table

install -m 755 bin/bltk	${RPM_BUILD_ROOT}%{_libdir}/bltk/bin

install -m 755 lib/libxse.so.0	${RPM_BUILD_ROOT}%{_libdir}/bltk/lib/libxse.so.0

install -m 755 bin/bltk_*	${RPM_BUILD_ROOT}%{_libdir}/bltk/bin/
install -m 755 bin/bat_*	${RPM_BUILD_ROOT}%{_libdir}/bltk/bin/

install -m 755 wl_developer/bin/bltk_wl_developer ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_developer/bin
install -m 755 wl_developer/bin/bltk_wl_developer_xse ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_developer/bin
install -m 755 wl_developer/bin/bltk_wl_developer_spy ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_developer/bin

install -m 755 wl_game/bin/bltk_wl_game ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_game/bin
install -m 755 wl_game/bin/bltk_wl_game_xse ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_game/bin

install -m 755 wl_office/bin/bltk_wl_office ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office/bin
install -m 755 wl_office/bin/bltk_wl_office_xse ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office/bin
install -m 755 wl_office/bin/bltk_wl_office_run_app ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office/bin
install -m 644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office
install -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office
install -m 644 %{SOURCE4} ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office
install -m 644 wl_office/scen ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office
install -m 644 wl_office/scen_install ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office
install -m 644 wl_office/response_install ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office
install -m 644 wl_office/text* ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_office

install -m 755 wl_player/bin/bltk_wl_player ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_player/bin
install -m 755 wl_player/bin/bltk_wl_player_make_binary ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_player/bin

install -m 755 wl_reader/bin/bltk_wl_reader ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_reader/bin
install -m 755 wl_reader/bin/bltk_wl_reader_xse ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_reader/bin
install -m 644 wl_reader/war_and_peace.html ${RPM_BUILD_ROOT}%{_libdir}/bltk/wl_reader

cat << ":EOF" > ${RPM_BUILD_ROOT}%{_bindir}/bltk
#!/bin/sh

bltk_native="$(rpm --eval '%%{_libdir}')/bltk/bin/$(basename $0)"

[ -x "$bltk_native" ] && exec "$bltk_native" "$@"
exec /usr/lib/bltk/bin/$(basename $0) "$@"
:EOF
chmod a+rx ${RPM_BUILD_ROOT}%{_bindir}/bltk
pushd ${RPM_BUILD_ROOT}%{_bindir}
for f in bltk_plot bltk_report bltk_report_compress bltk_report_table bltk_report_uncompress;
do
  ln -s bltk $f
done
popd

%ldconfig_scriptlets

%files
%doc doc/HOWTO doc/Manual doc/README
%config(noreplace) %attr(0644,root,root) /etc/bltk.conf

%{_libdir}/bltk/bin/bltk
%{_bindir}/bltk
%{_bindir}/bltk_plot
%{_bindir}/bltk_report
%{_bindir}/bltk_report_compress
%{_bindir}/bltk_report_table
%{_bindir}/bltk_report_uncompress

%{_mandir}/man1/bltk*
%{_mandir}/man5/bltk.conf.*

%{_libdir}/bltk/lib/libxse.so.0

%{_libdir}/bltk/bin/bat_drain
%{_libdir}/bltk/bin/bat_drain_table
%{_libdir}/bltk/bin/bltk_calc
%{_libdir}/bltk/bin/bltk_check
%{_libdir}/bltk/bin/bltk_display_state
%{_libdir}/bltk/bin/bltk_get_ac_adapter
%{_libdir}/bltk/bin/bltk_get_bat
%{_libdir}/bltk/bin/bltk_get_cpufreq
%{_libdir}/bltk/bin/bltk_get_cpuinfo
%{_libdir}/bltk/bin/bltk_get_cpustat
%{_libdir}/bltk/bin/bltk_get_cpustate
%{_libdir}/bltk/bin/bltk_get_dmidecode
%{_libdir}/bltk/bin/bltk_get_hdparm
%{_libdir}/bltk/bin/bltk_get_hd_rpm
%{_libdir}/bltk/bin/bltk_get_info
%{_libdir}/bltk/bin/bltk_get_kernel_release
%{_libdir}/bltk/bin/bltk_get_lspci
%{_libdir}/bltk/bin/bltk_get_meminfo
%{_libdir}/bltk/bin/bltk_get_realpath
%{_libdir}/bltk/bin/bltk_get_stat
%{_libdir}/bltk/bin/bltk_get_system_release
%{_libdir}/bltk/bin/bltk_get_timer
%{_libdir}/bltk/bin/bltk_get_user_field
%{_libdir}/bltk/bin/bltk_get_xdpyinfo

%{_libdir}/bltk/bin/bltk_install
%{_libdir}/bltk/bin/bltk_func
%{_libdir}/bltk/bin/bltk_plot
%{_libdir}/bltk/bin/bltk_report
%{_libdir}/bltk/bin/bltk_report_check
%{_libdir}/bltk/bin/bltk_report_compress
%{_libdir}/bltk/bin/bltk_report_table
%{_libdir}/bltk/bin/bltk_report_uncompress
%{_libdir}/bltk/bin/bltk_save_sys_info
%{_libdir}/bltk/bin/bltk_spy
%{_libdir}/bltk/bin/bltk_time
%{_libdir}/bltk/bin/bltk_type_command
%{_libdir}/bltk/bin/bltk_winid
%{_libdir}/bltk/bin/bltk_wl_common

%{_libdir}/bltk/wl_developer/bin/bltk_wl_developer
%{_libdir}/bltk/wl_developer/bin/bltk_wl_developer_spy
%{_libdir}/bltk/wl_developer/bin/bltk_wl_developer_xse

%{_libdir}/bltk/wl_game/bin/bltk_wl_game
%{_libdir}/bltk/wl_game/bin/bltk_wl_game_xse

%{_libdir}/bltk/wl_office/bin/bltk_wl_office
%{_libdir}/bltk/wl_office/bin/bltk_wl_office_xse
%{_libdir}/bltk/wl_office/bin/bltk_wl_office_run_app
%{_libdir}/bltk/wl_office/OOCALC_FILE_SAMPLE.ods
%{_libdir}/bltk/wl_office/OODRAW_FILE_SAMPLE.odg
%{_libdir}/bltk/wl_office/OOWRITER_FILE_SAMPLE.odt
%{_libdir}/bltk/wl_office/scen
%{_libdir}/bltk/wl_office/scen_install
%{_libdir}/bltk/wl_office/response_install
%{_libdir}/bltk/wl_office/text1
%{_libdir}/bltk/wl_office/text2
%{_libdir}/bltk/wl_office/text3

%{_libdir}/bltk/wl_player/bin/bltk_wl_player
%{_libdir}/bltk/wl_player/bin/bltk_wl_player_make_binary

%{_libdir}/bltk/wl_reader/bin/bltk_wl_reader
%{_libdir}/bltk/wl_reader/bin/bltk_wl_reader_xse
%{_libdir}/bltk/wl_reader/war_and_peace.html

%changelog
%autochangelog
