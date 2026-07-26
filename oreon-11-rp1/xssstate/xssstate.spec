%global source0_hash c4b6f504a6a8eb247bc60960bd65cbf9631c008449a1d71ac4c55e34be1c6011

Name:          xssstate
Version:       1.1
Release:       27%{?dist}
Summary:       A simple tool to retrieve the X screen saver state
License:       MIT
URL:           http://tools.suckless.org/%{name}
Source0:       http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: libXScrnSaver-devel
BuildRequires: make
BuildRequires: sed

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -e 's|PREFIX = /usr/local|PREFIX = %{_prefix}|' \
    -e 's|LIBS = -L/usr/lib -lc -lX11 -lXss|LIBS = -L%{_libdir} -lc -lX11 -lXss|' \
    -e 's|CFLAGS = -g -std=c99 -pedantic -Wall -O0 ${INCS} ${CPPFLAGS}|CFLAGS = %{optflags} ${INCS} ${CPPFLAGS}|' \
   -i config.mk
sed -i 's|^\t@|\t|' Makefile
chmod -x xsidle.sh

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc LICENSE README xsidle.sh
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
%autochangelog
