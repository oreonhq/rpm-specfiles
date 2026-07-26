%global source0_hash 64ba620d04245535ea331c4ace2c7cc0940d1fec73926e09f0f386dbb92d5349

%global pkgname zyn

Summary:	LV2 port of the ZynAddSubFX engine
Name:		lv2-zynadd-plugins
Version:	1
Release:	37%{?dist}
# lv2-midi*.h is LGPLv2+
# but the rest is GPLv2. The whole plugin will be then:
License:	GPL-2.0-only
URL:		http://home.gna.org/zyn/
Source:		http://download.gna.org/%{pkgname}/%{pkgname}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:	fftw-devel
BuildRequires:	gcc-c++
BuildRequires:	lv2-devel
BuildRequires:	lv2dynparam-devel
Requires:	lv2
Provides:	%{pkgname} = %{version}-%{release}

%description
The zyn project main goal is to extract synth engines from ZynAddSubFX and pack
them in LV2 plugin format. Resulting plugins are heavily based on work made by
Nasca Octavian Paul. If you like the amazing sounds these plugins generate you
should thank Paul for this.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

# Don't hide anything
sed -i 's|\t@|\t|' GNUmakefile

# lv2core seemingly permanently renamed to lv2 at version 1.16
sed -i s/lv2core/lv2/g GNUmakefile
find . -type f -name '*.c' | xargs sed -i "s/lv2dynparam\//lv2dynparam1\/lv2dynparam\//g"

%build
make %{?_smp_mflags} \
	CFLAGS="%{optflags} -fPIC -DPIC \
	$(pkg-config --cflags fftw3 lv2core lv2dynparamplugin1)" \
	CXXFLAGS="%{optflags}" \
	LDFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_libdir}/lv2
make LV2_INSTALL_PATH=%{buildroot}%{_libdir}/lv2 install

%files
%doc AUTHORS README
%license gpl.txt
%{_libdir}/lv2/zynadd.lv2/

%changelog
%autochangelog
