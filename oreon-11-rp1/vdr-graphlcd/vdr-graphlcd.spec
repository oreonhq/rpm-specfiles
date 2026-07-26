%global source0_hash f4e395c7fadc898550a1d7942af96df951de3116de245c1e5009aceb3af2587a

%global rname   vdr-plugin-graphlcd
%global sname   graphlcd

# Set vdr_version based on Fedora version
# Default
%global vdr_version 2.6.9

%if 0%{?fedora} == 42
%global vdr_version 2.7.4
%elif 0%{?fedora} == 43
%global vdr_version 2.7.7
%elif 0%{?fedora} >= 44
%global vdr_version 2.8.1
%endif

Name:           vdr-graphlcd
Version:        1.0.8
Release:        9%{?dist}
Summary:        VDR plugin: Output to graphic LCD
License:        GPL-2.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-graphlcd
Source0:        https://github.com/vdr-projects/%{rname}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.conf.sample
Source3:        %{name}-fonts.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  graphlcd-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       dejavu-sans-fonts
Requires:       bitstream-vera-sans-fonts

%description
graphlcd is a plugin for the Video Disc Recorder and shows information
about the current state of VDR on displays supported by the GraphLCD
driver library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{rname}-%{version}

# W: file-not-utf8
iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY

%build
%make_build

%install
%make_install SKIP_INSTALL_DOC=1

# remove bundling fonts
rm -rf %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/{DejaVuSans-Bold,DejaVuSansCondensed}.ttf
ln -s %{_datadir}/fonts/dejavu/{DejaVuSans-Bold,DejaVuSansCondensed}.ttf \
  %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/

rm -rf %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/{Vera,VeraBd}.ttf
ln -s %{_datadir}/fonts/bitstream-vera/{Vera,VeraBd}.ttf \
  %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/

install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf

install -Dpm 644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf.sample

install -Dpm 644 %{SOURCE3} \
    %{buildroot}%{vdr_resdir}/plugins/%{sname}/fonts.conf

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%dir %{vdr_resdir}/plugins/%{sname}
%{vdr_resdir}/plugins/%{sname}/fonts
%{vdr_resdir}/plugins/%{sname}/logos
%{vdr_resdir}/plugins/%{sname}/skins
%config(noreplace) %{vdr_resdir}/plugins/%{sname}/*.alias
%config(noreplace) %{vdr_resdir}/plugins/%{sname}/fonts.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf.sample

%changelog
%autochangelog
