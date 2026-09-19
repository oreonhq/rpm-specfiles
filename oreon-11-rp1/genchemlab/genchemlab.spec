%global source0_hash bd200ff30c406faf5da3637d4887a438be689c537cf0886d881dc890745a43ea

Summary: A general chemistry lab experiment simulator
Name: genchemlab
Version: 1.0
Release: 44%{?dist}
License: GPL-2.0-or-later
Source0: http://kent.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
URL: http://genchemlab.sourceforge.net/
Patch0: gcl-desktop.patch
BuildRequires:  gcc-c++
BuildRequires: qt3-devel freeglut-devel desktop-file-utils
BuildRequires: make

%description
GenChemLab is an OpenGL-based application intended to simulate several common 
general chemistry experiments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
sed -i 's/\r//' GPL.txt
sed -i 's/\r//' COPYRIGHT.txt
%patch -P0 -p1

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
	--delete-original \
	%{buildroot}%{_datadir}/applications/genchemlab.desktop

%files
%doc COPYRIGHT.txt GPL.txt HISTORY.txt README.txt
%{_datadir}/%{name}/
%{_bindir}/genchemlab
%{_datadir}/pixmaps/genchemlab.png
%{_datadir}/applications/genchemlab.desktop

%changelog
%autochangelog
