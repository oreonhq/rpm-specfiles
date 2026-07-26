%global source0_hash 1c195ad2d4b5d3918f53d23f59db8bb766bd3e2b3fa3de5da5ebdb1bcc1c3c61

Name:		domoticz
Version:	2025.2
Release:	4%{?dist}
Summary:	Open source Home Automation System

License:	GPL-3.0-or-later AND Apache-2.0 AND BSL-1.0 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:		http://www.domoticz.com
Source0:	https://github.com/domoticz/domoticz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source0:	https://github.com/domoticz/domoticz/archive/%%{git_short_hash}.tar.gz#/%%{name}-%%{version}.tar.gz
Source1:	%{name}.service
Source2:	%{name}.conf
# Manually update version reported inside app
Source3:	%{name}-appversion
# https://github.com/Thalhammer/jwt-cpp/tree/71c3d36507183ceb74b9cf10d1232fe1223bdfb0
Source4:	jwt-cpp-71c3d36507183ceb74b9cf10d1232fe1223bdfb0.zip

# Use system tinyxpath (https://github.com/domoticz/domoticz/pull/1759)
Patch1:		%{name}-tinyxpath.patch
# Fix python detection (https://github.com/domoticz/domoticz/pull/1749)
Patch2:		%{name}-python.patch
# Python linking fix
Patch3:		%{name}-python-link.patch
# Boost 1.90 support (https://github.com/domoticz/domoticz/pull/6488)
#                    (https://github.com/domoticz/domoticz/pull/6487)
Patch4:		%{name}-boost.patch

BuildRequires:	boost-devel
BuildRequires:	cereal-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	fmt-devel
BuildRequires:	fontpackages-devel
BuildRequires:	gcc-c++
BuildRequires:	git
BuildRequires:	jsoncpp-devel
BuildRequires:	libopenzwave-devel >= 1.6.0
BuildRequires:	lua-devel
BuildRequires:	make
BuildRequires:	minizip-compat-devel
BuildRequires:	mosquitto-devel
BuildRequires:	openssl-devel
BuildRequires:	python3-devel
BuildRequires:	sqlite-devel
BuildRequires:	systemd-devel
BuildRequires:	tinyxpath-devel
BuildRequires:	zlib-devel

Requires(post):	systemd
Requires(postun):	systemd
Requires(preun):	systemd

Requires:	google-droid-sans-fonts
Recommends:	mosquitto
Recommends:	system-python-libs >= 3.4
#Recommends:	zwave-js-ui

Provides:	bundled(js-ace)
Provides:	bundled(js-angularamd) = 0.2.1
Provides:	bundled(js-angularjs) = 1.5.8
Provides:	bundled(js-blockly)
Provides:	bundled(js-bootbox)
Provides:	bundled(js-bootstrap) = 3.2.0
Provides:	bundled(js-colpick)
Provides:	bundled(js-d3)
Provides:	bundled(js-datatables-datatools) = 2.2.3
Provides:	bundled(js-dateformat) = 1.2.3
Provides:	bundled(js-filesaver) = 0.0-git20140725
Provides:	bundled(js-highcharts) = 4.2.6
Provides:	bundled(js-html5shiv) = 3.6.2
Provides:	bundled(js-i18next) = 1.8.0
Provides:	bundled(js-jquery) = 1.12.0
Provides:	bundled(js-ngdraggable)
Provides:	bundled(js-nggrid)
Provides:	bundled(js-jquery-noty) = 2.1.0
Provides:	bundled(js-require) = 2.1.14
Provides:	bundled(js-respond) = 1.1.0
Provides:	bundled(js-angular-ui-bootstrap) = 0.13.4
Provides:	bundled(js-wow) = 0.1.9
Provides:	bundled(js-ozwcp)
Provides:	bundled(js-less) = 1.3.0
Provides:	bundled(js-ion-sound) = 3.0.6
Provides:	bundled(js-zeroclipboard) = 1.0.4
Provides:	bundled(jwt-cpp) = 0.0-git20241116

%global _python_bytecompile_extra 0

%description
Domoticz is a Home Automation System that lets you monitor and configure various
devices like: Lights, Switches, various sensors/meters like Temperature, Rain,
Wind, UV, Electra, Gas, Water and much more. Notifications/Alerts can be sent to
any mobile device

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{name}-%{version}
# Add support for future versions of Python by replacing hardcoded version with macro
sed -i 's/-lpythonVER/-lpython%{python3_version}/' CMakeLists.txt
# Renaming of old define used wrong case in ZWave file
sed -i 's/sTypeSetPoint/sTypeSetpoint/g' hardware/ZWaveBase.cpp
rm -rf sqlite/
rm -rf tinyxpath/
cp -p %{SOURCE3} ./appversion.h
# jwt-cpp external bundled library
unzip -d extern %{SOURCE4}
rmdir extern/jwtcpp/
mv extern/jwt-cpp-71c3d36507183ceb74b9cf10d1232fe1223bdfb0/ extern/jwtcpp/

# Create a sysusers.d config file
cat >domoticz.sysusers.conf <<EOF
u domoticz - 'Domoticz Home Automation Server' %{_datadir}/%{name} -
m domoticz dialout
EOF

%build
%cmake \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DUSE_STATIC_LIBSTDCXX=NO \
 -DUSE_STATIC_OPENZWAVE=NO \
 -DUSE_OPENSSL_STATIC=NO \
 -DUSE_BUILTIN_JSONCPP=NO \
 -DUSE_BUILTIN_LIBFMT=NO \
 -DUSE_BUILTIN_LUA=NO \
 -DUSE_BUILTIN_MINIZIP=NO \
 -DUSE_BUILTIN_MQTT=NO \
 -DUSE_BUILTIN_SQLITE=NO \
 -DUSE_BUILTIN_TINYXPATH=NO \
 -DUSE_STATIC_BOOST=NO \
 -DCMAKE_INSTALL_PREFIX=%{_datadir}/%{name} \
 %{nil}
%cmake_build

%install
%cmake_install

# remove bundled OpenZWave configuration files so system files are used
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/Config/

# remove docs, we grab them in files below
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*.txt

# move binary to standard directory
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/

# install systemd service and config
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
mkdir -p $RPM_BUILD_ROOT%{_unitdir}/
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

# create backups/database/plugins/scripts/ssl cert directory
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/{backups,plugins,scripts,templates}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/{dzVents,lua,lua_parsers,python,templates}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/{data,generated_scripts,scripts}

# Unbundle DroidSans.ttf
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/elemental/fonts/DroidSans.ttf
ln -s %{_fontdir}/google-droid/DroidSans.ttf \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/elemental/fonts/
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-light/fonts/DroidSans.ttf
ln -s %{_fontdir}/google-droid/DroidSans.ttf \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-light/fonts/
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-dark/fonts/DroidSans.ttf
ln -s %{_fontdir}/google-droid/DroidSans.ttf \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-dark/fonts/

# Link default plugins and scripts to userdata directory
ln -s %{_datadir}/%{name}/scripts/dzVents/data/README.md \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/data/README.md
ln -s %{_datadir}/%{name}/scripts/dzVents/generated_scripts/README.md \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/generated_scripts/README.md
ln -s %{_datadir}/%{name}/scripts/dzVents/scripts/README.md \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/scripts/README.md
ln -s %{_datadir}/%{name}/scripts/templates/All.{dzVents,Lua,Python} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Bare.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Device.{dzVents,Lua} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/global_data.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Group.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/HTTPRequest.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Scene.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Security.{dzVents,Lua} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Time.Lua \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Timer.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/UserVariable.{dzVents,Lua} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/

# Link web page templates to userdata directory
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/www/templates/{custom.example,readme.txt} \
   $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/templates
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/www/templates
ln -s %{_sharedstatedir}/%{name}/templates \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/templates

# Byte compile the default plugin
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/plugins/AwoxSMP

install -m0644 -D domoticz.sysusers.conf %{buildroot}%{_sysusersdir}/domoticz.conf

%pretrans
# Handle directory move for a few releases
rm -rf %{_datadir}/%{name}/www/templates

%pre
# For OpenZWave USB access (/dev/ttyACM#)
usermod -G domoticz,dialout domoticz

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license License.txt
%doc README.md History.txt
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_datadir}/%{name}/
%attr(0755,domoticz,domoticz) %{_sharedstatedir}/%{name}/
%{_unitdir}/%{name}.service
%{_sysusersdir}/domoticz.conf

%changelog
%autochangelog
