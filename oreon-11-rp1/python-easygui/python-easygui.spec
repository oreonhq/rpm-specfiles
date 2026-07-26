%global source0_hash 37c44f1b8ed811e08ca18f49e3363bb7b25665370f4d5e0c0b670ae91ac1c037

%global upstream_name easygui

Name:           python-easygui
Version:        0.96
Release:        51%{?dist}
Summary:        Very simple, very easy GUI programming in Python

#License file, says CC 2.0 upstream website says with this version they moved to BSD.
License:        BSD-3-Clause
URL:            http://easygui.sourceforge.net/
# Source doesn't follow the normal SF convention since upstream isn't using the SF Files system.
Source0:        http://easygui.sourceforge.net/download/version%{version}/easygui_v%{version}_docs.tar.gz
Source1:        easygui-LICENSE.txt

BuildArch:      noarch
BuildRequires: python%{python3_pkgversion}-devel

%global _description\
Experienced Pythonistas need support for quick and dirty GUI features. New\
Python programmers need GUI capabilities that don't require any knowledge\
of Tkinter, frames, widgets, callbacks or lambda. This is what EasyGUI\
provides. Using EasyGUI, all GUI interactions are invoked by simple\
function calls.\
\
EasyGUI is different from other GUIs in that EasyGUI is NOT event-driven.\
It allows you to program in a traditional linear fashion, and to put up\
dialogs for simple input and output when you need to. If you have not yet\
learned the event-driven paradigm for GUI programming, EasyGUI will allow\
you to be productive with very basic tasks immediately. Later, if you\
wish to make the transition to an event-driven GUI paradigm, you can do\
so with a more powerful GUI package such as anygui, PythonCard, Tkinter,\
wxPython, etc.

%description %_description

%package -n python%{python3_pkgversion}-%{upstream_name}
Summary:        Very simple, very easy GUI programming in Python3
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-tkinter

%description -n python%{python3_pkgversion}-%{upstream_name}
Experienced Pythonistas need support for quick and dirty GUI features. New 
Python programmers need GUI capabilities that don't require any knowledge 
of Tkinter, frames, widgets, callbacks or lambda. This is what EasyGUI 
provides. Using EasyGUI, all GUI interactions are invoked by simple 
function calls.

EasyGUI is different from other GUIs in that EasyGUI is NOT event-driven. 
It allows you to program in a traditional linear fashion, and to put up 
dialogs for simple input and output when you need to. If you have not yet 
learned the event-driven paradigm for GUI programming, EasyGUI will allow 
you to be productive with very basic tasks immediately. Later, if you 
wish to make the transition to an event-driven GUI paradigm, you can do 
so with a more powerful GUI package such as anygui, PythonCard, Tkinter, 
wxPython, etc. 
This package allows for use of easygui with Python 3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc %{upstream_name}-%{version}

rm -rf %{py3dir}
cp -a . %{py3dir}

%generate_buildrequires
%pyproject_buildrequires

%build
pushd %{py3dir}
%pyproject_wheel
popd

%install
pushd %{py3dir}
%pyproject_install
popd

install -m 644 %{SOURCE1} .

%files -n python%{python3_pkgversion}-%{upstream_name}
%doc easygui_license_info.txt cookbook/ easygui_pydoc.html easygui_version_info.html epydoc/ faq/ pydoc/ tutorial/
%doc easygui-LICENSE.txt
%{python3_sitelib}/easygui*
%{python3_sitelib}/__pycache__/easygui.cpython-3*.py*

%changelog
%autochangelog
