%global source0_hash none

Name:           primer3
Version:        2.4.0
Release:        17%{?dist}
Summary:        PCR primer design tool
# Automatically converted from old format: BSD and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later
URL:            http://primer3.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++

%description
Primer3 is a widely used program for designing PCR primers (PCR = 
"Polymerase Chain Reaction"). PCR is an essential and ubiquitous 
tool in genetics and molecular biology. Primer3 can also design 
hybridization probes and sequencing primers.

PCR is used for many different goals. Consequently, primer3 has 
many different input parameters that you control and that tell 
primer3 exactly what characteristics make good primers for your goals.

%prep
%autosetup
chmod -x src/*
chmod +x src/primer3_config # causes permissions issue if removed
sed -i -e 's|CFLAGS  = $(CC_OPTS) $(O_OPTS)|CFLAGS  = $(CC_OPTS) $(O_OPTS) $(INIT_CFLAGS) -fpermissive|' src/Makefile
sed -i 's/\r//' settings_files/*
sed -i -e 's|/opt/primer3_config|/etc/primer3_config|' src/release_notes.txt src/thal_main.c src/primer3_boulder_main.c

%build
cd src
export INIT_CFLAGS="%{optflags}"
%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 src/%{name}_core $RPM_BUILD_ROOT%{_bindir}/%{name}_core
install -p -m 0755 src/oligotm $RPM_BUILD_ROOT%{_bindir}/oligotm
install -p -m 0755 src/ntdpal $RPM_BUILD_ROOT%{_bindir}/ntdpal
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/primer3_config
cp -r src/primer3_config $RPM_BUILD_ROOT%{_sysconfdir}/

%check
pushd src
 %{?_with_tests:make test}
popd

%files
%doc README.md example settings_files/*
%license LICENSE
%{_bindir}/%{name}_core
%{_bindir}/oligotm
%{_bindir}/ntdpal
%{_sysconfdir}/primer3_config

%changelog
%autochangelog
