%global source0_hash 07a25600f49bb0fbca2488f889be31d8b346ef48aca7e3979c441b52c6dbb528

Name:           python-svg
Version:        0.2.2b
Release:        46%{?dist}
Summary:        Python wrapper for svg

License:        BSD-2-Clause-Views
URL:            http://code.google.com/p/pysvg/
Source0:        http://pysvg.googlecode.com/files/pysvg-0.2.2b.zip
Patch0:         pysvg-python3.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
pySVG is a pure Python library to create/load and manipulate SVG documents.\
\
Its main use is to "code" svg images.

%description %_description

%package -n python3-svg
Summary: %summary
%{?python_provide:%python_provide python3-svg}

%description -n python3-svg %_description

%package doc
Summary: Documentation for python-syg
Requires: python3-svg = %{version}-%{release}

%description doc %_description

These are the documentation files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn pysvg-%{version}

%patch -P0 -p1 -b .python3

rm -f doc/html/.buildinfo

# Convert to utf-8
for file in `find . -name '*.py'`; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

#Strip bad EOL encodings
for file in `find . -name '*.txt'` doc/html/_static/pygments.css; do
 sed -i "s|\r||g" $file
done
for file in `find . -name '*.py'`; do
 sed -i "s|\r||g" $file
done

#Remove shabangs.
for lib in `find . -name '*.py'`; do
 sed -i '/\/usr\/bin\/python/d' $lib
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

find $RPM_BUILD_ROOT -name '*.egg-info' | xargs rm -rf

%files doc
%doc doc/

%files -n python3-svg
%doc doc/license.txt
%{python3_sitelib}/pysvg*

%changelog
%autochangelog
