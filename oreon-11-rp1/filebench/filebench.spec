%global source0_hash a1d1516083a1d46bccf6246caf709e800e93eccf17572583343e77726b720678

Name:           filebench
Version:        1.4.9.1
Release:        24%{?dist}
Summary:        A model based file system workload generator

License:        CDDL
URL:            http://filebench.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        LICENSE
Source2:        filebench.1
Patch0:         make-dofile-global.patch
Patch1:         filebench-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires: make

%description
Filebench is a file system and storage benchmark that allows to generate a
high variety of workloads. It employs extensive Workload Model Language (WML)
for detailed workload specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .dofile
%patch -P1 -p1 -b .c99
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%build
%configure
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
