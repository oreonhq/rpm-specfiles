%global source0_hash 54ca11c9c71d1bc530908f7f68d0a6021c871d283bdc1b421d8776ba8b456302
Name:           yapet
Version:        2.6
Release:        1%{?dist}
Summary:        Yet Another Password Encryption Tool
License:        LicenseRef-Callaway-GPLv3+-with-exceptions
URL:            http://yapet.guengel.ch/
Source0:        http://%{name}.guengel.ch/downloads/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libargon2-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
# /oreon:deps
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

%configure --disable-install-doc   \
           --disable-source-doc    \
           --disable-install-doci  \
           --disable-silent-rules
%make_build
%install
%make_install
rm -frv %{buildroot}%{_datadir}/applications/
rm -frv %{buildroot}%{_docdir}
%find_lang %{name}
%find_lang libyacurs
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
