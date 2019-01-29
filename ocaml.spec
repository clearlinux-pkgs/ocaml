Name     : ocaml
Version  : 4.07.0
Release  : 7
URL      : http://caml.inria.fr/pub/distrib/ocaml-4.07/ocaml-4.07.0.tar.xz
Source0  : http://caml.inria.fr/pub/distrib/ocaml-4.07/ocaml-4.07.0.tar.xz
Patch1   : 0001-configure-Allow-user-defined-C-compiler-flags.patch
Summary  : programming language
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires : ocaml-bin
Requires : ocaml-lib
BuildRequires : ocaml
BuildRequires : util-linux

%package bin
License:        GPL-2.0 LGPL-2.1
Summary:        programming language
Group:          doc
Requires:       ocaml-lib

%description bin
programming language

%package lib
License:        GPL-2.0 LGPL-2.1
Summary:        programming language
Group:          doc
Provides:	ocaml(runtime) = %{version}

%description lib
programming language

%description
OCaml is an industrial strength programming language supporting functional,
imperative and object-oriented styles

%package doc
License:        GPL-2.0 LGPL-2.1
Summary:        programming language
Group:          doc

%description doc
programming language

%prep
%setup -q -n ocaml-4.07.0
%patch1 -p1

%build
export LANG=C
./configure -prefix /usr -libdir /usr/lib64/ocaml -fPIC
make world.opt %{?_smp_mflags}

%install
rm -rf %{buildroot}
make PREFIX=%{buildroot}/usr MANDIR=%{buildroot}/usr/share/man LIBDIR=%{buildroot}/usr/lib64/ocaml install
find %{buildroot} -name '*.cmt' -a -delete
find %{buildroot} -name '*.cmti' -a -delete

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/*
%exclude /usr/bin/ocaml-instr-report

%files lib
%defattr(-,root,root,-)
/usr/lib64/ocaml/*

%files doc
%defattr(-,root,root,-)
/usr/share/man/*
