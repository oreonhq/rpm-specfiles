%global source0_hash none

%global vname dist426

Name:		autodocksuite
Version:	4.2.6
Release:	27%{?dist}
Summary:	AutoDock is a suite of docking tools to study protein-ligand interaction

License:	GPL-2.0-or-later
URL:		http://autodock.scripps.edu/
Source0:	http://autodock.scripps.edu/downloads/autodock-registration/tars/%{vname}/%{name}-%{version}-src.tar.gz

BuildRequires:  gcc-c++
BuildRequires:	csh
BuildRequires: make

%description
AutoDock is a suite of automated docking tools. It is designed to predict \
how small molecules, such as substrates or drug candidates, bind to a \
receptor of known 3D structure. AutoDock 4 actually consists of two main \
programs: autodock performs the docking of the ligand to a set of grids \
describing the target protein; autogrid pre-calculates these grids. In \
addition to using them for docking, the atomic affinity grids can be \
visualized. This can help, for example, to guide organic synthetic chemists \
design better binders.

%prep
%setup -q -n src

%build

pushd autodock
%configure
make %{?_smp_mflags}
popd

pushd %{_builddir}/src/autogrid
%configure
make V=1 %{?_smp_mflags}

%install
make -C autodock install DESTDIR=%{buildroot}
make -C autogrid install DESTDIR=%{buildroot}

rm -f %{buildroot}/%{_bindir}/autodock4.omp

%files
%license autodock/COPYING
%{_bindir}/autodock4
%{_bindir}/autogrid4

%changelog
%autochangelog
