%global source0_hash 534eb65f01c4b89b366e1251ec1c13a03482574e580f08107f1ed8ad1994bc67

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     florist
%global upstream_version  22.0.0
%global upstream_gittag   v%{upstream_version}

Name:           florist
Epoch:          2
Version:        %{upstream_version}
Release:        15%{?dist}
Summary:        Open Source implementation of the POSIX Ada Bindings

License:        GPL-2.0-or-later WITH GNAT-exception

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source:         %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# C 99 compatibility in the configure script, submitted upstream:
# https://github.com/AdaCore/florist/pull/10
Patch0:         florist-configure-c99.patch
# C 99 compatibility in c-posix.c, backported:
# https://github.com/AdaCore/florist/commit/e6c2f95ff8ae426c3d832f23aa80bcda82dcfa5c
Patch1:         florist-c99.patch

# The following patches have been downloaded from a fork of Florist that
# continued public maintenance of the library while it was not available through
# AdaCore's GitHub page. See the patch files for details.

# [Bugfix] https://github.com/AdaCore/florist/issues/6
Patch:          %{name}-fix-locking-full-size-file-even-when-growing.patch
# [Bugfix] https://github.com/AdaCore/florist/issues/7
Patch:          %{name}-fix-number-of-elements-to-write.patch

BuildRequires:  fedora-gnat-project-common
BuildRequires:  gprbuild gcc-gnat
BuildRequires:  make sed
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Florist is an implementation of the IEEE Standards 1003.5: 1992, \
IEEE STD 1003.5b: 1996, and parts of IEEE STD 1003.5c: 1998, \
also known as the POSIX Ada Bindings. Using this library, \
you can call operating system services from within Ada programs.

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

%autosetup -p1

###########
## Build ##
###########

%build
%configure --enable-shared

%{make_build} GPRBUILD_FLAGS='%{GPRbuild_optflags} -XLIBRARY_TYPE=relocatable' \
     GCCFLAGS='%{build_cflags}' VERSION=%{version} TARGET=

#############
## Install ##
#############

%install
# Use GPRinstall directly to have full control over the installation.
gprinstall %{GPRinstall_flags} --no-manifest --no-build-var \
           -XLIBRARY_TYPE=relocatable \
           florist.gpr

# Fix up the symlink.
ln --symbolic --force lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/%{name}");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/%{name}";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}*.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 4: Replace the value of Library_Dir with Directories.Libdir.
# 5: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.

###########
## Files ##
###########

%files
%doc README
%license COPYING
%{_libdir}/lib%{name}.so.1

%files devel
%{_GNAT_project_dir}/%{name}.gpr
%dir %{_includedir}/%{name}
# Exclude some junk that doesn't belong under /usr/include:
%exclude %{_includedir}/%{name}/*.[ch]
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/%{name}/*.ad[sb]
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}.so

###############
## Changelog ##
###############

%changelog
%autochangelog
