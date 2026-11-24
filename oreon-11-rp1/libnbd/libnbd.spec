# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 71865fc41ccb56a5e8fe3ab29da2a61006df2a7a25f72011ab10fca40aa5c920
%global source1_hash 397d5ef5648432911b10249d5a010a7abe50f06decfb8aca22b55a4a2bb6c521
%global source2_hash f4755cb63a4cd176444099772d659a0f449751ae5b8f1428c78de4c02a01b1bb
%global source3_hash ada8bf19a266d8b7e7b1bf7c3be680eafb7c03b8f8b87b7cec3f113682e53d88
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%ifnarch %{ix86}
%if !0%{?oreon}
%global have_ocaml 1
%endif
%endif

%if !0%{?rhel} && !0%{?oreon}
%global have_ublk 1
%endif

%if !0%{?rhel} && !0%{?oreon}
%ifnarch %{ix86}
%global have_nbd_ko 1
%endif
%endif

%global verify_tarball_signature 1

%global source_directory 1.25-development

Name:           libnbd
Version:        1.25.9
Release:        1%{?dist}
Summary:        NBD client library in userspace

License:        LGPL-2.0-or-later AND BSD-3-Clause
URL:            https://gitlab.com/nbdkit/libnbd

Source0:        http://libguestfs.org/download/libnbd/%{source_directory}/%{name}-%{version}.tar.gz
Source1:        http://libguestfs.org/download/libnbd/%{source_directory}/%{name}-%{version}.tar.gz.sig
Source2:       https://download.libguestfs.org/rich@annexia.org-pubkey.txt

Source3:        copy-patches.sh

%if 0%{verify_tarball_signature}
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  openpgpverify
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  make
BuildRequires:  /usr/bin/pod2man
BuildRequires:  gnutls-devel
BuildRequires:  libxml2-devel

BuildRequires:  fuse3
BuildRequires:  fuse3-devel

%if 0%{?have_ublk}
BuildRequires:  liburing-devel >= 2.2
BuildRequires:  ubdsrv-devel >= 1.0-3.rc6
%endif

BuildRequires:  python3-devel

%if 0%{?have_ocaml}
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
%endif

BuildRequires:  glib2-devel

BuildRequires:  bash-completion
%if 0%{?fedora} || 0%{?rhel} >= 11 || 0%{?oreon}
BuildRequires:  bash-completion-devel
%endif

BuildRequires:  coreutils
BuildRequires:  glibc-utils
BuildRequires:  gnutls-utils
BuildRequires:  iproute
BuildRequires:  jq
%if 0%{?have_nbd_ko}
BuildRequires:  nbd
%endif
BuildRequires:  util-linux

%ifnarch %{ix86}
%if !0%{?oreon}
BuildRequires:  qemu-img
BuildRequires:  nbdkit
BuildRequires:  nbdkit-data-plugin
BuildRequires:  nbdkit-eval-plugin
BuildRequires:  nbdkit-memory-plugin
BuildRequires:  nbdkit-null-plugin
BuildRequires:  nbdkit-pattern-plugin
BuildRequires:  nbdkit-sh-plugin
BuildRequires:  nbdkit-sparse-random-plugin
%endif
%endif

%description
NBD — Network Block Device — is a protocol for accessing Block Devices
(hard disks and disk-like things) over a Network.

This is the NBD client library in userspace, a simple library for
writing NBD clients.

The key features are:

 * Synchronous and asynchronous APIs, both for ease of use and for
   writing non-blocking, multithreaded clients.

 * High performance.

 * Minimal dependencies for the basic library.

 * Well-documented, stable API.

 * Bindings in several programming languages.

%package devel
Summary:        Development headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development headers for %{name}.

%if 0%{?have_ocaml}
%package -n ocaml-%{name}
Summary:        OCaml language bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}
This package contains OCaml language bindings for %{name}.

%package -n ocaml-%{name}-devel
Summary:        OCaml language development package for %{name}
Requires:       ocaml-%{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}-devel
This package contains OCaml language development package for
%{name}.  Install this if you want to compile OCaml software which
uses %{name}.
%endif

%package -n python3-%{name}
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%global __provides_exclude_from ^%{python3_sitearch}/lib.*\\.so

%description -n python3-%{name}
python3-%{name} contains Python 3 bindings for %{name}.

%package -n nbdfuse
Summary:        FUSE support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     fuse3

%description -n nbdfuse
This package contains FUSE support for %{name}.

%if 0%{?have_ublk}
%package -n nbdublk
Summary:        Userspace NBD block device
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     kernel >= 6.0.0
Recommends:     %{_sbindir}/ublk

%description -n nbdublk
This package contains a userspace NBD block device
based on %{name}.
%endif

%package bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name} = %{version}-%{release}

%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
%if 0%{verify_tarball_signature}
%{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1
autoreconf -i

%build
%configure \
    --disable-static \
    --with-extra='%{name}-%{version}-%{release}' \
    --with-tls-priority=@LIBNBD,SYSTEM \
    --with-bash-completions \
    PYTHON=%{__python3} \
    --enable-python \
%if 0%{?have_ocaml}
    --enable-ocaml \
%else
    --disable-ocaml \
%endif
    --enable-fuse \
    --disable-golang \
    --disable-rust \
%if 0%{?have_ublk}
    --enable-ublk \
%else
    --disable-ublk \
%endif
    %{nil}

make %{?_smp_mflags}

%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -delete

rm $RPM_BUILD_ROOT%{_mandir}/man3/libnbd-golang.3*

%if !0%{?have_ocaml}
rm $RPM_BUILD_ROOT%{_mandir}/man3/libnbd-ocaml.3*
%endif

%check
function skip_test ()
{
    for f in "$@"; do
        rm -f "$f"
        echo 'exit 77' > "$f"
        chmod +x "$f"
    done
}

%if 0%{?rhel}
skip_test interop/interop-qemu-storage-daemon.sh
%endif

skip_test fuse/test-*.sh

make -C tests connect-tcp6 ||:
skip_test tests/connect-tcp6

make %{?_smp_mflags} check || {
    for f in $(find -name test-suite.log); do
        echo
        echo "==== $f ===="
        cat $f
    done
    exit 1
  }

%files
%doc README.md
%license COPYING.LIB
%{_bindir}/nbdcopy
%{_bindir}/nbddump
%{_bindir}/nbdinfo
%{_libdir}/libnbd.so.*
%{_mandir}/man1/nbdcopy.1*
%{_mandir}/man1/nbddump.1*
%{_mandir}/man1/nbdinfo.1*

%files devel
%doc TODO.md examples/*.c
%license examples/LICENSE-FOR-EXAMPLES
%{_includedir}/libnbd.h
%{_libdir}/libnbd.so
%{_libdir}/pkgconfig/libnbd.pc
%{_mandir}/man3/libnbd.3*
%{_mandir}/man1/libnbd-release-notes-1.*.1*
%{_mandir}/man3/libnbd-security.3*
%{_mandir}/man3/nbd_*.3*

%if 0%{?have_ocaml}
%files -n ocaml-%{name}
%dir %{_libdir}/ocaml/nbd
%{_libdir}/ocaml/nbd/META
%{_libdir}/ocaml/nbd/*.cma
%{_libdir}/ocaml/nbd/*.cmi
%{_libdir}/ocaml/stublibs/dllmlnbd.so
%{_libdir}/ocaml/stublibs/dllmlnbd.so.owner

%files -n ocaml-%{name}-devel
%doc ocaml/examples/*.ml
%license ocaml/examples/LICENSE-FOR-EXAMPLES
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/nbd/*.cmxa
%{_libdir}/ocaml/nbd/*.cmx
%endif
%{_libdir}/ocaml/nbd/*.a
%{_libdir}/ocaml/nbd/*.mli
%{_mandir}/man3/libnbd-ocaml.3*
%{_mandir}/man3/NBD.3*
%{_mandir}/man3/NBD.*.3*
%endif

%files -n python3-%{name}
%{python3_sitearch}/libnbdmod*.so
%{python3_sitearch}/nbd.py
%{python3_sitearch}/nbdsh.py
%{python3_sitearch}/__pycache__/nbd*.py*
%{_bindir}/nbddiscard
%{_bindir}/nbdsh
%{_bindir}/nbdzero
%{_mandir}/man1/nbddiscard.1*
%{_mandir}/man1/nbdsh.1*
%{_mandir}/man1/nbdzero.1*
%{_mandir}/man3/libnbd-python.3*

%files -n nbdfuse
%{_bindir}/nbdfuse
%{_mandir}/man1/nbdfuse.1*

%if 0%{?have_ublk}
%files -n nbdublk
%{_bindir}/nbdublk
%{_mandir}/man1/nbdublk.1*
%endif

%files bash-completion
%if 0%{?fedora} || 0%{?rhel} >= 11
%dir %{bash_completions_dir}
%{bash_completions_dir}/nbdcopy
%{bash_completions_dir}/nbddiscard
%{bash_completions_dir}/nbddump
%{bash_completions_dir}/nbdfuse
%{bash_completions_dir}/nbdinfo
%{bash_completions_dir}/nbdsh
%if 0%{?have_ublk}
%{bash_completions_dir}/nbdublk
%endif
%{bash_completions_dir}/nbdzero
%else
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/nbdcopy
%{_datadir}/bash-completion/completions/nbddiscard
%{_datadir}/bash-completion/completions/nbddump
%{_datadir}/bash-completion/completions/nbdfuse
%{_datadir}/bash-completion/completions/nbdinfo
%{_datadir}/bash-completion/completions/nbdsh
%if 0%{?have_ublk}
%{_datadir}/bash-completion/completions/nbdublk
%endif
%{_datadir}/bash-completion/completions/nbdzero
%endif

%changelog
%autochangelog
