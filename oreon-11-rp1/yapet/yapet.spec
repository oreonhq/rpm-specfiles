%global source0_hash 54ca11c9c71d1bc530908f7f68d0a6021c871d283bdc1b421d8776ba8b456302

#global pre pre2

Name:           yapet
Version:        2.6
Release:        8%{?pre}%{?dist}
Summary:        Yet Another Password Encryption Tool
# Automatically converted from old format: GPLv3+ with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv3+-with-exceptions
URL:            http://yapet.guengel.ch/
Source0:        http://yapet.guengel.ch/downloads/%{name}-%{version}%{?pre}.tar.xz
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  cppunit-devel
BuildRequires:  libargon2-devel

%if 0%{?rhel} == 7
BuildRequires:  devtoolset-7-gcc-c++
%endif

%description
YAPET is a text based password manager using the AES-256 encryption
algorithm to store passwords and associated information encrypted on
disk. Its primary aim is to provide a safe way to store passwords in a
file on disk while having a small footprint, and compiling and running
under today's most popular Unix Systems.

The password records are protected by a master password which is used
to encrypt and decrypt the password records.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}%{?pre}

%build
%if 0%{?rhel} == 7
source /opt/rh/devtoolset-7/enable
%endif

%configure --disable-install-doc   \
           --disable-source-doc    \
           --disable-install-doci  \
           --disable-silent-rules

%make_build

%install
%make_install
# Console running is OK.
rm -frv %{buildroot}%{_datadir}/applications/

# %%doc instead.
rm -frv %{buildroot}%{_docdir}

%find_lang %{name}
%find_lang libyacurs

%check
# RNG tests need /dev/urandom OR /dev/random!
# Failed at messagebox1. Digging.
#make check

%files -f %{name}.lang -f libyacurs.lang
%doc AUTHORS BUGS NEWS README
%license COPYING LICENSE
%{_bindir}/*yapet*
%{_mandir}/man*/*yapet*

%changelog
%autochangelog
