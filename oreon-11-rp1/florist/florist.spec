%global source0_hash 534eb65f01c4b89b366e1251ec1c13a03482574e580f08107f1ed8ad1994bc67
%global upstream_owner    AdaCore
%global upstream_name     florist
%global upstream_version  22.0.0
%global upstream_gittag   v%{upstream_version}
Name:           florist
Epoch:          2
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        Open Source implementation of the POSIX Ada Bindings
License:        GPL-2.0-or-later WITH GNAT-exception
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{name}/archive/%{upstream_gittag}/%{name}-%{version}.tar.gz
Patch0:         florist-configure-c99.patch
Patch1:         florist-c99.patch
Patch:          %{name}-fix-locking-full-size-file-even-when-growing.patch
Patch:          %{name}-fix-number-of-elements-to-write.patch
ExclusiveArch:  %{GPRbuild_arches}
%global common_description_en \
Florist is an implementation of the IEEE Standards 1003.5: 1992, \
IEEE STD 1003.5b: 1996, and parts of IEEE STD 1003.5c: 1998, \
also known as the POSIX Ada Bindings. Using this library, \
you can call operating system services from within Ada programs.
# oreon:deps
BuildRequires:  fedora-gnat-project-common
BuildRequires:  gcc-gnat
BuildRequires:  gprbuild
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description %{common_description_en}

#################
## Subpackages ##
#################

%package devel
Summary:    Development files for Florist
Requires:   fedora-gnat-project-common
Requires:   %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel %{common_description_en}

The florist-devel package contains source code and linking information for
developing applications that use Florist.

#############
## Prepare ##
#############

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-shared
%{make_build} GPRBUILD_FLAGS='%{GPRbuild_optflags} -XLIBRARY_TYPE=relocatable' \
     GCCFLAGS='%{build_cflags}' VERSION=%{version} TARGET=
%install
gprinstall %{GPRinstall_flags} --no-manifest --no-build-var \
           -XLIBRARY_TYPE=relocatable \
           florist.gpr
ln --symbolic --force lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/%{name}");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/%{name}";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}*.gpr
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n florist-devel -f %{oreon_filedir}/florist-devel.list

%changelog

%autochangelog
