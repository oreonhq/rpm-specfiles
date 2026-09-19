%global source0_hash 3bd560309fd6d70b14bbb8230e1baf8706b804eb6201220bb6c3d6db72003d1b

# the upstream name is io_lib, but it was deemed too generic, and
# staden-io_lib will be more recognizable for users
Name:           staden-io_lib
Version:        1.14.8
Release:        7%{?dist}
Summary:        General purpose library to handle gene sequencing machine trace files

License:        MIT
URL:            http://staden.sourceforge.net
Source0:        http://downloads.sourceforge.net/staden/io_lib-%{version}.tar.gz
Patch0:         staden-libs-config.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  curl-devel zlib-devel

%description
The Staden I/O library provides a general purpose interface for reading and
writing trace files and other bioinformatics experiment files.  The programmer
simply calls, for example, the read_reading function to create a "Read" C
structure with the data loaded into memory.  It has been compiled and tested
on a variety of Unix systems, MacOS X and MS Windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n io_lib-%{version} -p1

# libread is too generic. Make up something more specific.
# Also fix config script name to include the "staden-" part.
mv io_lib-config.in staden-io_lib-config.in
sed -i 's/libread/libstaden-read/g' io_lib/Makefile.in progs/Makefile.in
sed -i 's/lread/lstaden-read/' staden-io_lib-config.in
sed -i 's/io_lib-config/staden-io_lib-config/g' configure Makefile.in

%build
%configure --disable-static
# make sure /lib64 /usr/lib64 are known to libtool to avoid rpath issues
sed -i 's+\(search_path_spec=\"\)+\1/lib64 /usr/lib64 +' libtool
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets

%global so_version 11
%files
%doc README COPYRIGHT CHANGES docs/
%{_libdir}/*.so.%{so_version}
%{_libdir}/*.so.%{so_version}.*
%{_bindir}/append_sff
%{_bindir}/convert_trace
%{_bindir}/cram_dump
%{_bindir}/cram_index
%{_bindir}/cram_size
%{_bindir}/extract_fastq
%{_bindir}/extract_qual
%{_bindir}/extract_seq
%{_bindir}/get_comment
%{_bindir}/hash_exp
%{_bindir}/hash_extract
%{_bindir}/hash_list
%{_bindir}/hash_sff
%{_bindir}/hash_tar
%{_bindir}/index_tar
%{_bindir}/makeSCF
%{_bindir}/scf_dump
%{_bindir}/scf_info
%{_bindir}/scf_update
%{_bindir}/scram_flagstat
%{_bindir}/scram_merge
%{_bindir}/scram_pileup
%{_bindir}/scram_test
%{_bindir}/scramble
%{_bindir}/srf2fasta
%{_bindir}/srf2fastq
%{_bindir}/srf_dump_all
%{_bindir}/srf_extract_hash
%{_bindir}/srf_extract_linear
%{_bindir}/srf_filter
%{_bindir}/srf_index_hash
%{_bindir}/srf_info
%{_bindir}/srf_list
%{_bindir}/trace_dump
%{_bindir}/ztr_dump
%{_mandir}/man1/*

%files devel
%doc
%{_mandir}/man3/*
%{_mandir}/man4/*
%{_includedir}/io_lib/
%{_libdir}/*.so
%{_bindir}/staden-io_lib-config

%changelog
%autochangelog
