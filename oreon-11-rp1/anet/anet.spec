%global source0_hash 9f6f9aa48078b7a6c636a64a0ded749c3475049cbf74efb251a8339091de8e30

Name:           anet
Version:        0.5.1
Release:        8%{?dist}
Summary:        Ada Networking Library

License:        GPL-2.0-or-later WITH GNAT-exception
URL:            https://www.codelabs.ch/anet/
Source:         https://www.codelabs.ch/download/libanet-%{version}.tar.bz2
Source2:        https://www.codelabs.ch/download/libanet-%{version}.tar.bz2.sig
Source5:        https://www.codelabs.ch/keys/0xDBF6D7E1095FD0D9.asc
# Disable one test that doesn't work in Koji:
Patch:          anet-0.3.3-no_IPv6_multicast_test.patch

BuildRequires:  gcc-gnat fedora-gnat-project-common make ahven-devel
BuildRequires:  gprbuild
BuildRequires:  gpgverify
BuildRequires:  asciidoctor
BuildRequires:  sed
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Anet is a networking library for the Ada programming language. It supports, \
among other things, IPv6, Unix domain sockets, multicast, raw sockets, link \
layer sockets and Netlink.

%global common_description_sv \
Anet är ett nätverksprogrammeringsbibliotek för programmeringsspråket ada. \
Det har bland annat stöd för IPv6, Unixsocketar, flersändning, råa socketar, \
länklagersocketar och Netlink.

%description %{common_description_en}

%description -l sv %{common_description_sv}

%package devel
Summary:        Development files for Anet
Summary(sv):    Filer för programmering med Anet
License:        GPL-2.0-or-later WITH GNAT-exception AND MIT
# Asciidoctor inserts an MIT-licensed stylesheet in the manual.
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use Anet.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder Anet.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE5}' --signature='%{SOURCE2}' --data='%{SOURCE0}'
%autosetup -n libanet-%{version} -p0

# Override the upstream usage of control-flow checking with Fedora's arch-
# dependent choice because GCC doesn't offer control-flow checking for all
# arches.
%global fix_cf_protection %([[ '%{build_adaflags}' = *-fcf-protection* ]] || echo -fcf-protection=none)
# This expands to an empty string if "-fcf-protection" is found among Fedora's
# compiler flags, and to "-fcf-protection=none" if it's not found.

%define all_the_flags "GNAT_BUILDER_FLAGS=%{GNAT_builder_flags}" "ADAFLAGS=%{build_adaflags} %{fix_cf_protection}" "LDFLAGS=%{build_ldflags}"
# define makes the macro lazily expanded, unlike global.

%build
make %{all_the_flags}
make build-doc

%install
# Pass all_the_flags here too to ensure that GPRbuild won't recompile anything.
%{make_install} %{all_the_flags} GPRINSTALLFLAGS='%{GPRinstall_flags}'

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/%{name}");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/%{name}";|i' \
    %{buildroot}%{_GNAT_project_dir}/*.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 4: Replace the value of Library_Dir with Directories.Libdir.
# 5: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.

%check
# Disable the hardening hack only for the testsuite.
# https://bugzilla.redhat.com/show_bug.cgi?id=1197501
# all_the_flags must be lazily expanded for this to work.
%undefine _hardened_build
make tests %{all_the_flags}

%files
%{_libdir}/*.so.*
%license COPYING
%doc AUTHORS

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/%{name}
%{_GNAT_project_dir}/*
%doc README TODO obj/html examples

%changelog
%autochangelog
