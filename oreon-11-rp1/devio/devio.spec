%global source0_hash a71e87f49f52cd90dbd45431f65e83d18e073fb2669f91c29c59019b175cd5a8

Name:           devio
Version:        1.2
Release:        35%{?dist}
Summary:        Read and write utility for block devices

License:        MIT
URL:            http://devio.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.man
Patch0:         devio-configure-c99.patch

BuildRequires:  gcc
BuildRequires: make

%description
devio is a command line utility intended to read and write on block devices.
The primary difference between devio and other command line utilities, such
as dd and cat, is that it is not stream based - it writes directly into
the object rather than reading and writing a stream of data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

install -Dp -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
