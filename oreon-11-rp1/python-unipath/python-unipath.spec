%global source0_hash 09839adcc72e8a24d4f76d63656f30b5a1f721fc40c9bcd79d8c67bdd8b47dae

%global        oname Unipath
Summary:       Alternative to Python modules os, os.path and shutil
Name:          python-unipath
Version:       1.1
Release:       35%{?dist}
License:       MIT
URL:           https://pypi.python.org/pypi/Unipath/
Source0:       https://files.pythonhosted.org/packages/source/U/%{oname}/%{oname}-%{version}.tar.gz
BuildArch:     noarch
BuildRequires: python3-devel
%global _description\
Unipath is a package for doing pathname calculations and filesystem\
access in an object-oriented manner, an alternative to functions in\
os.path, shutil and glob, and even some functions in os.* It's based\
on Jason Orendorffs path.py but does not adhere as strictly to the\
underlying functions' syntax, in order to provide more user\
convenience and higher-level functionality. For example:\
\
 o p.mkdir() succeeds silently if the directory already exists, and\
 o p.mkdir(True) creates intermediate directories a la os.makedirs.\
 o p.rmtree(parents=True) combines shutil.rmtree, os.path.isdir,\
   os.remove, and os.removedirs, to recursively remove whatever it is\
   if it exists.\
 o p.read_file("rb") returns the file's contents in binary mode.\
 o p.needs_update([other_path1, ...]) returns True if p doesn't exist\
   or has an older timestamp than any of the others.\
 o extra convenience functions in the unipath.tools module. dict2dir\
   creates a directory hierarchy described by a dict. dump_path displays\
   an ASCII tree of a directory hierarchy.

%description %_description

%package -n     python3-unipath
Summary:        %summary
%description -n python3-unipath %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{oname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files unipath -L

%files -n python3-unipath -f %{pyproject_files}
%license CHANGES
%doc BUGS.txt PKG-INFO README.html README.rst

%changelog
%autochangelog
