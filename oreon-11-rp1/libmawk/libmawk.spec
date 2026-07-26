%global source0_hash 18db04b5931968f5cb9864e0009578a57ef449e8f2997bedbc829ce55f2dc2b1

Name:           libmawk
Version:        1.0.5
Release:        1%{?dist}
Summary:        Embed awk scripting language in any application written in C

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://repo.hu/projects/libmawk
Source0:        http://repo.hu/projects/libmawk/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
Libmawk is a fork of mawk 1.3.3 restructured for embedding.
This means the user gets libmawk.h and libmawk.so and can embed
awk scripting language in any application written in C.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
HTML documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# This ./configure command refers to scconfig. See http://repo.hu/projects/scconfig/
./"configure" --prefix=%{_prefix} --libarchdir=%{_lib} --symbols \
  --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags}"
%make_build

%install
%make_install LIBARCHDIR=%{buildroot}/%{_libdir} LIBPATH=%{buildroot}/%{_libdir}/%{name}

%files
%license src/libmawk/COPYING
%doc AUTHORS README Release_notes
%{_libdir}/*.so.1
%{_libdir}/*.so.1.0*
%{_bindir}/lmawk
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.awk
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc %{_docdir}/%{name}

%changelog
%autochangelog
