%global source2_hash 3e4e7cbafe00365ee0b78bc7f26aea55bdaf54e6de657d0b9b4ad5dc724ca2df
%global source1_hash 3a52ead118776e7b1ab6b4a58812c8fd5029cbfb23cc0f6a5558e7d13974d772
%global source0_hash 3f33b22135219c39c3c695f7b7171c2567d3e2a17c798c0a90607320cbb268f2
Name: ed
Version: 1.22.6
Release:        1%{?dist}
Summary:        The GNU line editor
License: GPL-2.0-only AND GFDL-1.3-no-invariants-or-later
URL:     https://www.gnu.org/software/ed/
Source0:        https://mirrors.kernel.org/gnu/ed/%{name}-%{version}.tar.lz
Source1:        https://mirrors.kernel.org/gnu/ed/%{name}-%{version}.tar.lz.sig
Source2: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x25B62C9821501AA0#./antoniodiazdiaz-keyring-2026.asc
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  lzip
BuildRequires:  make
# /oreon:deps
%description
ed is a line-oriented text editor, used to create, display, and modify text
files (both interactively and via shell scripts). For most purposes, ed has been
replaced in normal usage by full-screen editors (emacs and vi, for example).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%if 0%{?rhel} || (0%{?oreon} >= 11)
# no lzip in RHEL; bsdtar can handle it but not from within %%setup.
%setup -q -c -T
bsdtar -xf %{SOURCE0} -C %{_builddir}
%else
%autosetup
%endif

%build

%set_build_flags
./configure \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --datarootdir=%{_datadir} \
    --infodir=%{_infodir} \
    --mandir=%{_mandir} \
    --program-prefix=%{?_program_prefix} \
    CC="${CC-gcc}" \
    CPPFLAGS="${CPPFLAGS}" \
    CFLAGS="${CFLAGS}" \
    LDFLAGS="${LDFLAGS}"
%make_build
%install
%make_install
rm -vrf %{buildroot}%{_infodir}/dir
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.22.5-1
- Import
