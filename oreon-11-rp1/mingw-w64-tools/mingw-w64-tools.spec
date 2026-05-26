# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 5afe822af5c4edbf67daaf45eec61d538f49eef6b19524de64897c6b95828caf
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

#%%global snapshot_date 20140530
#%%global snapshot_rev 430863ffea2f6101fbfc0ee35ee098ab2f96b53c
#%%global snapshot_rev_short %%(echo %%{snapshot_rev} | cut -c1-6)
#%%global branch trunk

Name:           mingw-w64-tools
Version:        13.0.0
Release:        3%{?dist}
Summary:        Supplementary tools which are part of the mingw-w64 toolchain


# http://sourceforge.net/mailarchive/forum.php?thread_name=5157C0FC.1010309%40users.sourceforge.net&forum_name=mingw-w64-public
# The tools gendef and genidl are GPLv3+, widl is LGPLv2+
License:        GPL-3.0-or-later AND LGPL-2.0-or-later

URL:            http://mingw-w64.sourceforge.net/
%if 0%{?snapshot_date}
# To regenerate a snapshot:
# Use your regular webbrowser to open https://sourceforge.net/p/mingw-w64/mingw-w64/ci/%%{snapshot_rev}/tarball
# This triggers the SourceForge instructure to generate a snapshot
# After that you can pull in the archive with:
# spectool -g mingw-w64-tools.spec
Source0:        http://sourceforge.net/code-snapshots/git/m/mi/mingw-w64/mingw-w64.git/mingw-w64-mingw-w64-%{snapshot_rev}.zip
%else
Source0:        http://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}.tar.bz2
%endif

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  mingw32-filesystem >= 133
BuildRequires:  mingw64-filesystem >= 133
BuildRequires:  ucrt64-filesystem >= 133


%description
Supplementary tools which are part of the mingw-w64 toolchain
It contains gendef, genidl and mingw-w64-widl


%prep
%oreon_verify_sources
%if 0%{?snapshot_date}
rm -rf mingw-w64-v%{version}
mkdir mingw-w64-v%{version}
cd mingw-w64-v%{version}
unzip %{S:0}
%autosetup -p1 -D -T -n mingw-w64-v%{version}/mingw-w64-mingw-w64-%{snapshot_rev}
%else
%autosetup -p1 -n mingw-w64-v%{version}
%endif


%build
pushd mingw-w64-tools
    pushd gendef
        %configure
        make %{?_smp_mflags}
    popd

    pushd genidl
        %configure
        make %{?_smp_mflags}
    popd

    %ifnarch ppc64le s390x
    pushd widl
        # widl needs to be aware of the location of the IDL files belonging
        # to the toolchain. Therefore it needs to be built for both the win32
        # and win64 targets
        %global _configure ../configure
        mkdir win32
        pushd win32
          %configure --target=%{mingw32_target} --program-prefix=%{mingw32_target}- --with-widl-includedir=%{mingw32_includedir}
          %make_build
        popd
        mkdir win64
        pushd win64
          %configure --target=%{mingw64_target} --program-prefix=%{mingw64_target}- --with-widl-includedir=%{mingw64_includedir}
          %make_build
        popd
        mkdir ucrt64
        pushd ucrt64
          %configure --target=%{ucrt64_target} --program-prefix=%{ucrt64_target}- --with-widl-includedir=%{ucrt64_includedir}
          %make_build
        popd
    popd
    %endif
popd


%install
pushd mingw-w64-tools
    %make_install -C gendef
    %make_install -C genidl
    %ifnarch ppc64le s390x
    %make_install -C widl/win32
    %make_install -C widl/win64
    %make_install -C widl/ucrt64
    %endif
popd


%files
%license COPYING
%{_bindir}/gendef
%{_bindir}/genidl
%ifnarch ppc64le s390x
%{_bindir}/%{mingw32_target}-widl
%{_bindir}/%{mingw64_target}-widl
%{_bindir}/%{ucrt64_target}-widl
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.0-3
- Prepare for Oreon 11 (RP1)
