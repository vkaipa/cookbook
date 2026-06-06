"""
Recipe data for Vidya's Vegetarian Performance Cookbook.
To add a recipe, append a dict to the RECIPES list and re-run build_cookbook.py.
Tiers: "grab" | "easy" | "moderate" | "batch" | "snack"
"""

RECIPES = [

  # ── GRAB & GO ──────────────────────────────────────────────────────────────

  {
    "id": "berry-chia-pudding",
    "name": "Berry Chia Pudding",
    "tier": "grab", "tier_label": "Grab & Go",
    "chef": "Nigella Lawson",
    "description": "Prep in 5 minutes the night before. Slow-release carbs and omega-3s for long training sessions without morning crashes.",
    "time": "5 min prep + overnight chill", "servings": "1",
    "ingredients": ["4 tbsp chia seeds","1 cup full-fat coconut milk","½ cup milk (any)","1 tbsp maple syrup","½ tsp vanilla extract","½ cup mixed berries","2 tbsp walnuts, roughly chopped","Pinch of cinnamon"],
    "steps": ["Whisk chia seeds, coconut milk, milk, maple syrup, vanilla, and cinnamon together in a jar.","Cover and refrigerate overnight (minimum 4 hours).","In the morning, stir well, top with berries and walnuts. Add a splash more milk if too thick."],
    "macros": {"kcal": 320, "protein": 8, "carbs": 36, "fat": 16},
    "perf_tip": "Chia seeds are 40% omega-3 fatty acids — the most concentrated plant source available. This combination of slow and fast carbs makes it ideal as a pre-long-run breakfast."
  },

  {
    "id": "yogurt-parfait",
    "name": "Greek Yogurt Power Parfait",
    "tier": "grab", "tier_label": "Grab & Go",
    "chef": "Ina Garten",
    "description": "Layers of protein-rich yogurt, crunchy toasted seeds, and antioxidant-packed berries. Elegant simplicity at its best.",
    "time": "5 min", "servings": "1",
    "ingredients": ["1 cup full-fat Greek yogurt","¼ cup toasted puffed amaranth or puffed rice","2 tbsp mixed seeds (pepitas, sunflower)","½ cup mixed berries (fresh or frozen/thawed)","1 tbsp honey","½ tsp vanilla extract","Pinch of lemon zest"],
    "steps": ["Stir vanilla into yogurt.","Layer yogurt, seeds/puffs, and berries in a glass or jar.","Drizzle honey over the top and add lemon zest."],
    "macros": {"kcal": 380, "protein": 22, "carbs": 40, "fat": 10},
    "perf_tip": "Casein protein in Greek yogurt is slow-digesting — great as a post-evening-workout recovery snack before bed."
  },

  {
    "id": "avocado-egg-toast",
    "name": "Avocado Egg Toast",
    "tier": "grab", "tier_label": "Grab & Go",
    "chef": "Nigella Lawson",
    "description": "The performance athlete's reliable staple. Whole-grain toast, healthy fat from avocado, and complete amino acids from egg.",
    "time": "8 min", "servings": "1",
    "ingredients": ["2 slices whole-grain sourdough","1 ripe avocado","2 eggs","Juice of ½ lemon","Red pepper flakes","Everything bagel seasoning","Salt & black pepper","Small handful of rocket (optional)"],
    "steps": ["Toast the bread until golden and crisp.","Mash avocado with lemon juice, salt, and pepper.","Fry or poach eggs to your liking (3–4 min).","Spread avocado on toast, top with eggs, sprinkle everything seasoning and chilli flakes."],
    "macros": {"kcal": 380, "protein": 18, "carbs": 32, "fat": 20},
    "perf_tip": "Egg leucine triggers muscle protein synthesis. Pair this 1–2 hours pre-workout for sustained energy without GI distress."
  },

  {
    "id": "date-energy-bites",
    "name": "Date & Almond Energy Bites",
    "tier": "grab", "tier_label": "Grab & Go",
    "chef": "Martha Stewart",
    "description": "Batch-made in 15 minutes with no cooking required. Medjool dates are nature's energy gel — store a batch in the fridge all week.",
    "time": "15 min + 30 min chill (makes 12)", "servings": "2 bites",
    "ingredients": ["1 cup medjool dates, pitted (≈10 dates)","1 cup raw almonds","3 tbsp desiccated coconut flakes","2 tbsp almond butter","2 tbsp dark chocolate chips","1 tsp vanilla extract","Pinch of sea salt"],
    "steps": ["Blend dates and almonds in a food processor until roughly chopped and sticky.","Add remaining ingredients, pulse until combined (don't over-blend — keep texture).","Roll into 12 balls. Refrigerate 30 min. Store in fridge up to 2 weeks."],
    "macros": {"kcal": 165, "protein": 4, "carbs": 18, "fat": 9},
    "perf_tip": "Dates' glucose-to-fructose ratio closely mirrors commercial sports gels. Eat 1–2 bites 30 min before training for a fast, clean energy hit."
  },

  {
    "id": "chickpea-wrap",
    "name": "Chickpea & Hummus Wrap",
    "tier": "grab", "tier_label": "Grab & Go",
    "chef": "Yotam Ottolenghi",
    "description": "A no-cook wrap packed with plant protein, complex carbs, and bright Middle Eastern flavours. Builds in 5 minutes.",
    "time": "5 min", "servings": "1",
    "ingredients": ["1 large whole-wheat tortilla","3 tbsp hummus","½ cup canned chickpeas, drained & rinsed","Handful of baby spinach","¼ cucumber, sliced","2 tbsp crumbled feta","Drizzle of olive oil & lemon juice","Pinch of sumac or smoked paprika"],
    "steps": ["Lay tortilla flat and spread hummus across the centre.","Layer spinach, chickpeas, cucumber, and feta.","Drizzle lemon juice and olive oil, dust with sumac.","Fold the sides in, roll tightly. Wrap in foil if taking on the go."],
    "macros": {"kcal": 450, "protein": 18, "carbs": 54, "fat": 16},
    "perf_tip": "Chickpeas offer a low-GI carb load that sustains energy for 2–3 hours — ideal for long-distance or multi-set training days."
  },

  {
    "id": "tofu-scramble",
    "name": "Turmeric Tofu Scramble",
    "tier": "grab", "tier_label": "Grab & Go",
    "chef": "Ching-He Huang",
    "description": "High-protein, anti-inflammatory, and ready in 10 minutes. The turmeric + black pepper combo is one of the most evidence-backed combos in sports nutrition.",
    "time": "10 min", "servings": "1",
    "ingredients": ["250g extra-firm tofu, pressed and crumbled","½ tsp turmeric","½ tsp cumin","½ tsp smoked paprika","Handful of cherry tomatoes, halved","Handful of baby spinach","2 spring onions, sliced","1 tbsp soy sauce","1 tbsp olive oil","Black pepper (generous)"],
    "steps": ["Heat olive oil in a pan over medium-high. Add crumbled tofu and spread into a single layer.","Add turmeric, cumin, paprika, and black pepper. Stir and cook 3–4 min until edges start to crisp.","Add cherry tomatoes and soy sauce. Toss 1 min.","Add spinach, stir until just wilted. Top with spring onions."],
    "macros": {"kcal": 280, "protein": 22, "carbs": 14, "fat": 14},
    "perf_tip": "Piperine in black pepper increases curcumin (turmeric) bioavailability by up to 2000%. Tofu scramble delivers leucine — the key muscle-building amino acid — in under 10 minutes."
  },

  # ── EASY EVERYDAY ──────────────────────────────────────────────────────────

  {
    "id": "shakshuka",
    "name": "Classic Shakshuka",
    "tier": "easy", "tier_label": "Easy Everyday",
    "chef": "Yotam Ottolenghi",
    "description": "Eggs poached in a spiced tomato sauce — one pan, minimal effort, maximally satisfying. A Middle Eastern icon.",
    "time": "25 min", "servings": "2",
    "ingredients": ["1 can (400g) crushed tomatoes","4 eggs","1 red bell pepper, diced","1 onion, finely chopped","3 garlic cloves, minced","1 tsp cumin","1 tsp smoked paprika","½ tsp chilli flakes","2 tbsp olive oil","Salt & pepper","Fresh parsley & feta to serve"],
    "steps": ["Heat olive oil in a wide skillet over medium. Sauté onion until soft (5 min). Add garlic and pepper, cook 3 min.","Add spices, stir 30 sec. Pour in tomatoes, season well. Simmer 10 min.","Make 4 wells in the sauce. Crack in eggs. Cover and cook 5–7 min until whites are set.","Scatter feta and parsley. Serve with warm flatbread or sourdough."],
    "macros": {"kcal": 320, "protein": 20, "carbs": 24, "fat": 14},
    "perf_tip": "Lycopene in cooked tomatoes is a potent antioxidant that reduces exercise-induced oxidative stress. Eat this on training days."
  },

  {
    "id": "quinoa-bowl",
    "name": "Lemon Herb Quinoa Bowl",
    "tier": "easy", "tier_label": "Easy Everyday",
    "chef": "Yotam Ottolenghi",
    "description": "A complete protein powerhouse. Quinoa contains all 9 essential amino acids — rare in plant foods — with bright lemon and herbs.",
    "time": "20 min", "servings": "2",
    "ingredients": ["1 cup quinoa, rinsed","2 cups vegetable stock","½ cucumber, diced","1 cup cherry tomatoes, halved","¼ red onion, finely sliced","60g feta, crumbled","Large handful of fresh mint and parsley","Zest & juice of 1 lemon","3 tbsp olive oil","Salt & pepper"],
    "steps": ["Bring quinoa and stock to a boil, reduce to a simmer, cover, cook 15 min. Fluff and cool slightly.","Whisk lemon zest, juice, olive oil, salt, and pepper together.","Toss warm quinoa with dressing, then fold in cucumber, tomatoes, red onion, and herbs.","Top with feta. Serve warm or at room temp."],
    "macros": {"kcal": 480, "protein": 18, "carbs": 62, "fat": 16},
    "perf_tip": "Quinoa's complete amino acid profile makes it ideal post-workout. The carb-to-protein ratio (~3.5:1) is optimal for glycogen replenishment."
  },

  {
    "id": "bean-tacos",
    "name": "Black Bean Tacos & Mango Salsa",
    "tier": "easy", "tier_label": "Easy Everyday",
    "chef": "Rick Bayless",
    "description": "Mexico's street food wisdom adapted for performance athletes. Mango's fast carbs pair beautifully with slow-digesting beans.",
    "time": "20 min", "servings": "2 (4 tacos)",
    "ingredients": ["1 can black beans, drained","4 small corn tortillas","1 ripe mango, diced small","½ red onion, finely diced","1 jalapeño, minced","Juice of 2 limes","Fresh coriander","1 tsp cumin","1 tsp smoked paprika","1 tbsp olive oil","Greek yogurt or sour cream to serve","1 avocado, sliced"],
    "steps": ["Make salsa: combine mango, red onion, jalapeño, lime juice, and coriander. Season and set aside.","Heat oil in pan, add beans with cumin and paprika. Cook 5 min, mashing slightly.","Warm tortillas in a dry pan or directly over a gas flame.","Fill tortillas with beans, mango salsa, avocado, and a dollop of Greek yogurt."],
    "macros": {"kcal": 520, "protein": 20, "carbs": 72, "fat": 14},
    "perf_tip": "Mango vitamin C enhances non-heme iron absorption from the beans — critical for oxygen transport in endurance training."
  },

  {
    "id": "fried-rice",
    "name": "Vegetable Egg Fried Rice",
    "tier": "easy", "tier_label": "Easy Everyday",
    "chef": "Ching-He Huang",
    "description": "The best use for leftover rice. A 15-minute meal genuinely faster than ordering delivery — with better macros.",
    "time": "15 min (use day-old rice)", "servings": "2",
    "ingredients": ["2 cups day-old cooked brown rice","3 eggs","1 cup frozen peas & corn","2 spring onions, sliced","2 garlic cloves, minced","1 tsp fresh ginger, grated","2 tbsp soy sauce (or tamari)","1 tsp sesame oil","1 tbsp neutral oil","White pepper"],
    "steps": ["Heat wok or large pan over high heat until smoking. Add neutral oil.","Stir-fry garlic and ginger 30 sec. Add peas and corn, toss 2 min.","Push veg to side, scramble eggs in the pan until just set.","Add rice, break up clumps. Add soy sauce and toss over high heat. Finish with sesame oil and spring onions."],
    "macros": {"kcal": 440, "protein": 18, "carbs": 58, "fat": 14},
    "perf_tip": "Brown rice is higher in B vitamins (B1, B3, B6) than white — essential cofactors for converting carbohydrates into usable energy."
  },

  {
    "id": "miso-noodles",
    "name": "Miso Tofu Noodle Soup",
    "tier": "easy", "tier_label": "Easy Everyday",
    "chef": "Nobu Matsuhisa",
    "description": "Warming, restorative, and deeply nourishing. Miso's probiotics and soba's complex carbs make this an ideal recovery meal.",
    "time": "20 min", "servings": "2",
    "ingredients": ["80g soba noodles","200g firm tofu, cubed","½ cup frozen edamame","2 tbsp white miso paste","3 cups vegetable stock","2 spring onions, sliced","1 tsp soy sauce","½ tsp sesame oil","1 sheet nori, torn (optional)","Sesame seeds"],
    "steps": ["Cook soba noodles per packet, drain and set aside.","Bring stock to a simmer. Whisk in miso paste (never boil miso — kills probiotics).","Add tofu and edamame. Simmer gently 3–4 min.","Divide noodles between bowls. Ladle broth over. Top with spring onion, sesame seeds, and nori."],
    "macros": {"kcal": 380, "protein": 22, "carbs": 48, "fat": 10},
    "perf_tip": "Miso fermentation produces beneficial gut bacteria — important for athletes who train intensely and are prone to immune dips."
  },

  {
    "id": "chickpea-salad",
    "name": "Greek Chickpea Salad",
    "tier": "easy", "tier_label": "Easy Everyday",
    "chef": "Yotam Ottolenghi",
    "description": "A hearty salad that actually keeps you full. Bold Mediterranean flavours with real staying power.",
    "time": "10 min", "servings": "2",
    "ingredients": ["1 can chickpeas, drained","1 cucumber, diced","1 cup cherry tomatoes, halved","½ red onion, thinly sliced","½ cup Kalamata olives","100g feta, cubed","3 tbsp extra virgin olive oil","1.5 tbsp red wine vinegar","1 tsp dried oregano","Salt & pepper"],
    "steps": ["Combine chickpeas, cucumber, tomatoes, red onion, and olives in a large bowl.","Whisk olive oil, vinegar, oregano, salt, and pepper.","Pour dressing over salad and toss. Fold in feta gently. Rest 5 min before serving."],
    "macros": {"kcal": 420, "protein": 16, "carbs": 44, "fat": 18},
    "perf_tip": "Olive oil's oleocanthal has the same anti-inflammatory action as ibuprofen — eat this after intense training sessions to reduce DOMS."
  },

  {
    "id": "lentil-soup",
    "name": "Quick Red Lentil Soup",
    "tier": "easy", "tier_label": "Easy Everyday",
    "chef": "Claudia Roden",
    "description": "Minimal ingredients, profound flavour. Ready in 25 minutes and freezes beautifully.",
    "time": "25 min", "servings": "3",
    "ingredients": ["1 cup red lentils, rinsed","1 large onion, diced","3 garlic cloves, minced","1 carrot, diced","1 tsp cumin","½ tsp turmeric","4 cups vegetable stock","Juice of 1 lemon","2 tbsp olive oil","Salt & pepper","Pinch of chilli flakes for finishing"],
    "steps": ["Sauté onion and carrot in olive oil over medium heat until soft, 8 min. Add garlic, cumin, turmeric — stir 1 min.","Add lentils and stock. Bring to boil then simmer 15–18 min until lentils are completely soft.","Use an immersion blender to blend half the soup. Season and add lemon juice.","Finish with a drizzle of olive oil and pinch of chilli."],
    "macros": {"kcal": 340, "protein": 18, "carbs": 52, "fat": 6},
    "perf_tip": "Turmeric's curcumin significantly reduces DOMS. Pair with black pepper to increase curcumin absorption by 2000%."
  },

  {
    "id": "caprese-toast",
    "name": "White Bean & Caprese Toast",
    "tier": "easy", "tier_label": "Easy Everyday",
    "chef": "Marcella Hazan",
    "description": "Italian simplicity elevated: creamy white beans on sourdough with fresh mozzarella and basil oil.",
    "time": "15 min", "servings": "2",
    "ingredients": ["4 thick slices sourdough","1 can cannellini beans, drained","125g fresh mozzarella, torn","2 ripe tomatoes, sliced","Large handful of basil","3 tbsp extra virgin olive oil","1 garlic clove, halved","Balsamic glaze","Salt & pepper"],
    "steps": ["Toast bread until golden. Rub each slice with the cut garlic clove.","Mash beans with 1 tbsp olive oil, salt, and pepper. Spread generously on toast.","Layer tomato slices and torn mozzarella over the beans.","Tear basil over the top, drizzle with remaining olive oil and balsamic glaze."],
    "macros": {"kcal": 460, "protein": 22, "carbs": 50, "fat": 18},
    "perf_tip": "Cannellini beans are one of the best sources of phosphorus — critical for ATP production, which fuels every muscle contraction."
  },

  # ── MODERATE ───────────────────────────────────────────────────────────────

  {
    "id": "enchiladas",
    "name": "Sweet Potato & Black Bean Enchiladas",
    "tier": "moderate", "tier_label": "Moderate",
    "chef": "Diana Kennedy",
    "description": "Sweet potato and black beans are a nutritional dream team. The queen of Mexican cooking's principles applied here.",
    "time": "45 min", "servings": "3 (6 enchiladas)",
    "ingredients": ["6 corn tortillas","2 medium sweet potatoes, peeled & cubed","1 can black beans, drained","1.5 cups enchilada sauce (jarred)","½ cup grated cheddar","1 tsp cumin","1 tsp chilli powder","½ onion, diced","Olive oil","Greek yogurt, avocado, coriander to serve"],
    "steps": ["Preheat oven to 200°C. Toss sweet potato with olive oil, cumin, and chilli. Roast 20 min until tender.","Sauté onion until soft. Add beans and roasted sweet potato, season well.","Warm tortillas. Fill each with bean/potato mixture. Roll tightly and place seam-down in a baking dish.","Pour enchilada sauce over, top with cheese. Bake 15 min. Serve with yogurt, avocado, coriander."],
    "macros": {"kcal": 540, "protein": 20, "carbs": 74, "fat": 16},
    "perf_tip": "Sweet potato's beta-carotene converts to vitamin A, supporting immune health during heavy training blocks. The carb load here is ideal pre-race or competition day."
  },

  {
    "id": "mushroom-risotto",
    "name": "Mushroom & Spinach Risotto",
    "tier": "moderate", "tier_label": "Moderate",
    "chef": "Gordon Ramsay",
    "description": "Gordon's technique: hot stock, constant attention, finish with cold butter and Parmesan. Meditative cooking that yields something extraordinary.",
    "time": "40 min", "servings": "3",
    "ingredients": ["1.5 cups arborio rice","300g mixed mushrooms, sliced","Large handful of spinach","1 litre hot vegetable stock","1 onion, finely diced","3 garlic cloves, minced","½ cup dry white wine (or extra stock)","50g Parmesan, grated","2 tbsp cold butter","2 tbsp olive oil","Fresh thyme","Salt & pepper"],
    "steps": ["Heat stock in a separate saucepan — keep it gently simmering throughout.","Sauté onion in olive oil until soft. Add garlic. Add mushrooms on high heat — don't crowd them.","Add rice, stir to coat. Pour in wine, stir until absorbed. Add hot stock ladle by ladle, stirring constantly.","After 20–22 min, rice should be al dente. Remove from heat. Stir in butter and Parmesan vigorously. Fold in spinach."],
    "macros": {"kcal": 510, "protein": 18, "carbs": 66, "fat": 18},
    "perf_tip": "Mushrooms are the only vegetarian food to contain ergosterol, which converts to vitamin D2 — essential for muscle function and bone density in athletes."
  },

  {
    "id": "tikka-masala",
    "name": "Tofu Tikka Masala",
    "tier": "moderate", "tier_label": "Moderate",
    "chef": "Madhur Jaffrey",
    "description": "The godmother of Indian cooking's masala wisdom applied to tofu. Marinate overnight for maximum depth of flavour.",
    "time": "40 min (+ optional overnight marinade)", "servings": "3",
    "ingredients": ["400g extra-firm tofu, pressed & cubed","1 can crushed tomatoes","½ cup heavy cream or coconut cream","1 onion, finely diced","3 garlic cloves, minced","1 inch fresh ginger, grated","2 tsp garam masala","1 tsp cumin","1 tsp ground coriander","½ tsp turmeric","½ tsp chilli powder","3 tbsp Greek yogurt (for marinade)","2 tbsp neutral oil","Salt"],
    "steps": ["Marinate tofu in yogurt, 1 tsp garam masala, and chilli for at least 30 min (overnight is better).","Pan-fry marinated tofu until charred at edges, ~8 min. Set aside.","Sauté onion until golden. Blend onion, garlic, and ginger to a paste. Return to pan with all spices, fry 2 min.","Add tomatoes, simmer 10 min. Stir in cream and tofu. Simmer 5 min. Serve with basmati rice."],
    "macros": {"kcal": 420, "protein": 24, "carbs": 36, "fat": 18},
    "perf_tip": "Extra-firm tofu has ~17g protein per 100g — on par with chicken breast. The marinade step significantly improves the amino acid bioavailability."
  },

  {
    "id": "thai-curry",
    "name": "Thai Green Curry with Tofu",
    "tier": "moderate", "tier_label": "Moderate",
    "chef": "David Thompson",
    "description": "The secret is high heat, fresh aromatics, and never overcooking. Serve with jasmine rice for maximum carb fuel.",
    "time": "35 min", "servings": "3",
    "ingredients": ["400g firm tofu, cubed","1 can (400ml) coconut milk","2–3 tbsp green curry paste","1 cup jasmine rice (cook separately)","1 zucchini, sliced","1 cup sugar snap peas","1 red bell pepper, sliced","2 kaffir lime leaves","1 tbsp soy sauce","1 tsp palm sugar or brown sugar","Fresh Thai basil & lime to serve","1 tbsp neutral oil"],
    "steps": ["Heat a wok over high heat. Fry curry paste in 2 tbsp coconut milk for 2 min until fragrant.","Add remaining coconut milk and lime leaves. Bring to a boil.","Add tofu and vegetables. Simmer 8–10 min. Season with soy sauce and sugar.","Serve over jasmine rice with Thai basil and a squeeze of lime."],
    "macros": {"kcal": 490, "protein": 20, "carbs": 54, "fat": 20},
    "perf_tip": "Lemongrass in green curry paste has anti-inflammatory and analgesic properties that support recovery from heavy training."
  },

  {
    "id": "zucchini-fritters",
    "name": "Zucchini & Corn Fritters",
    "tier": "moderate", "tier_label": "Moderate",
    "chef": "Yotam Ottolenghi",
    "description": "Crispy outside, tender inside. Ottolenghi's trick: salt and drain the zucchini aggressively to prevent soggy fritters.",
    "time": "35 min", "servings": "2 (8 fritters)",
    "ingredients": ["3 medium zucchini, grated","1 cup corn kernels (fresh or frozen)","2 eggs","½ cup flour (or chickpea flour)","½ cup feta, crumbled","2 spring onions, sliced","Fresh mint and dill","Salt & pepper","Oil for frying","For tzatziki: 1 cup Greek yogurt, ½ cucumber grated & squeezed, 1 garlic clove, dill, lemon juice"],
    "steps": ["Salt grated zucchini generously. Leave 10 min, then squeeze out all moisture with a clean cloth.","Mix zucchini, corn, eggs, flour, feta, herbs, and spring onions. Season well.","Make tzatziki: mix yogurt with cucumber, garlic, dill, and lemon.","Heat 2 tbsp oil in non-stick pan over medium-high. Drop spoonfuls, flatten slightly. Cook 3 min per side until golden."],
    "macros": {"kcal": 400, "protein": 18, "carbs": 42, "fat": 16},
    "perf_tip": "Using chickpea flour adds extra protein and makes these naturally gluten-free. The yogurt-based tzatziki adds gut-friendly probiotics."
  },

  {
    "id": "stuffed-peppers",
    "name": "Stuffed Peppers with Quinoa & Feta",
    "tier": "moderate", "tier_label": "Moderate",
    "chef": "Ina Garten",
    "description": "The Barefoot Contessa's approach: good quality ingredients, minimal fuss. These look impressive but are genuinely easy.",
    "time": "45 min", "servings": "4",
    "ingredients": ["4 large bell peppers, tops cut off & seeds removed","1 cup quinoa, cooked","1 can chickpeas, drained","100g feta, crumbled","1 cup cherry tomatoes, halved","1 zucchini, diced small","2 garlic cloves, minced","1 tsp cumin","Handful of fresh parsley","Olive oil, salt & pepper"],
    "steps": ["Preheat oven to 200°C. Place peppers in a baking dish, drizzle with olive oil, season. Roast 15 min.","Sauté garlic and zucchini 3 min. Mix with quinoa, chickpeas, tomatoes, herbs, and feta. Season well.","Fill peppers with the quinoa mixture. Return to oven for 20 min until peppers are tender and tops are golden."],
    "macros": {"kcal": 420, "protein": 16, "carbs": 52, "fat": 14},
    "perf_tip": "Bell peppers have 3× the vitamin C of oranges — critical for collagen synthesis in joints and tendons under repeated training stress."
  },

  {
    "id": "buddha-bowl",
    "name": "Roasted Veg Buddha Bowl",
    "tier": "moderate", "tier_label": "Moderate",
    "chef": "Yotam Ottolenghi",
    "description": "Ottolenghi's love of roasting transforms humble veg into something deeply caramelised and satisfying. A customisable performance template.",
    "time": "40 min", "servings": "2",
    "ingredients": ["1 cup brown rice or farro, cooked","1 sweet potato, cubed","1 cup broccoli florets","½ red onion, wedged","1 can chickpeas, drained & patted dry","2 tbsp olive oil, salt, cumin, paprika","2 handfuls of kale or spinach","1 avocado, sliced","For tahini dressing: 3 tbsp tahini, 2 tbsp lemon juice, 1 garlic clove, 2 tbsp olive oil, water to thin, salt"],
    "steps": ["Preheat oven to 220°C. Toss sweet potato and broccoli with olive oil and spices on a baking tray. Roast 25–30 min.","On a separate tray, roast chickpeas 20 min until crispy.","Blend tahini dressing until smooth, thinning with water as needed.","Build bowls: grain base, roasted veg, crispy chickpeas, avocado, greens. Drizzle generously with tahini dressing."],
    "macros": {"kcal": 560, "protein": 20, "carbs": 70, "fat": 20},
    "perf_tip": "Tahini is rich in calcium, zinc, and magnesium — electrolytes lost in sweat that are often under-replaced in vegetarian athletes."
  },

  {
    "id": "stuffed-shells",
    "name": "Spinach & Ricotta Stuffed Shells",
    "tier": "moderate", "tier_label": "Moderate",
    "chef": "Marcella Hazan",
    "description": "Marcella's Italian canon simplified: fresh ricotta, good Parmesan, and patience. These freeze well — make a double batch.",
    "time": "45 min", "servings": "4",
    "ingredients": ["20 large pasta shells (conchiglioni)","400g ricotta","300g frozen spinach, thawed & squeezed dry","2 eggs","80g Parmesan, grated","Pinch of nutmeg","Salt & pepper","2 cups marinara or passata","Extra Parmesan for topping"],
    "steps": ["Preheat oven to 190°C. Cook shells to just under al dente. Drain and cool.","Mix ricotta, spinach, eggs, Parmesan, nutmeg, salt, and pepper until combined.","Spread marinara in the base of a baking dish. Fill each shell and arrange on top of sauce.","Spoon more sauce over shells. Top with Parmesan. Cover with foil, bake 20 min. Uncover and bake 10 min more."],
    "macros": {"kcal": 520, "protein": 28, "carbs": 58, "fat": 18},
    "perf_tip": "Ricotta's whey protein is the fastest-absorbing dairy protein. Eat this post-workout for quick amino acid delivery to muscles."
  },

  {
    "id": "saag-paneer",
    "name": "Saag Paneer",
    "tier": "moderate", "tier_label": "Moderate",
    "chef": "Madhur Jaffrey",
    "description": "Paneer is one of the highest-protein vegetarian whole foods. Paired with spinach and whole spices, this is performance food disguised as comfort food.",
    "time": "40 min", "servings": "3",
    "ingredients": ["400g paneer, cubed","500g fresh spinach (or 300g frozen, thawed)","1 onion, finely diced","3 garlic cloves, minced","1 inch fresh ginger, grated","1 green chilli","1 tsp cumin seeds","1 tsp garam masala","½ tsp turmeric","½ cup Greek yogurt","2 tbsp ghee or neutral oil","Salt"],
    "steps": ["Blanch spinach 2 min, drain, then blend coarsely. Set aside.","Fry paneer cubes in ghee until golden on each side. Remove and set aside.","In same pan, fry cumin seeds until popping. Add onion and cook until golden. Add garlic, ginger, chilli, and dry spices.","Add spinach purée and yogurt. Stir over medium heat 5 min. Return paneer, simmer 5 min more. Serve with roti or rice."],
    "macros": {"kcal": 460, "protein": 26, "carbs": 28, "fat": 26},
    "perf_tip": "Spinach is rich in dietary nitrates which convert to nitric oxide, improving blood flow and oxygen delivery to muscles during aerobic exercise."
  },

  # ── BATCH MEALS ────────────────────────────────────────────────────────────

  {
    "id": "red-lentil-dal",
    "name": "Red Lentil Dal",
    "tier": "batch", "tier_label": "Batch Meal",
    "chef": "Madhur Jaffrey",
    "description": "The workhorse of the book. Cheap, protein-packed, improves with age in the fridge, and reheats in 90 seconds. Make this every week.",
    "time": "50 min", "servings": "5–6",
    "ingredients": ["2 cups red lentils, rinsed","1 can (400ml) coconut milk","1 can crushed tomatoes","3 cups vegetable stock","1 large onion, diced","4 garlic cloves, minced","2 inch ginger, grated","2 tsp cumin","1.5 tsp turmeric","1 tsp garam masala","1 tsp ground coriander","Juice of 1 lemon","2 tbsp coconut oil or ghee","Fresh coriander to serve"],
    "steps": ["Heat fat in a large pot. Sauté onion until deep golden, ~10 min. Add garlic and ginger, cook 2 min.","Add all spices except garam masala. Fry 1 min. Add tomatoes and cook down 5 min.","Add lentils, stock, and coconut milk. Bring to boil, reduce to simmer. Cook 25–30 min until lentils are broken down.","Add garam masala and lemon juice. Adjust seasoning. Keeps 5 days in fridge, 3 months frozen."],
    "macros": {"kcal": 380, "protein": 22, "carbs": 54, "fat": 8},
    "perf_tip": "Lentils provide 36% of daily iron needs per serving — critical for haemoglobin production and oxygen transport in endurance athletes."
  },

  {
    "id": "moroccan-stew",
    "name": "Moroccan Chickpea Stew",
    "tier": "batch", "tier_label": "Batch Meal",
    "chef": "Paula Wolfert",
    "description": "Paula Wolfert's decades of North African research distilled here: sweet-savoury-spiced and deeply anti-inflammatory.",
    "time": "55 min", "servings": "5",
    "ingredients": ["2 cans chickpeas, drained","2 cans crushed tomatoes","2 cups vegetable stock","1 large onion, diced","3 garlic cloves, minced","2 carrots, sliced","1 sweet potato, cubed","2 tsp ras el hanout","1 tsp cumin","½ tsp cinnamon","½ cup dried apricots, halved","1 tbsp harissa paste","Lemon juice, fresh coriander, toasted almonds to serve"],
    "steps": ["Sauté onion until soft. Add garlic, carrots, sweet potato, spices, and harissa. Stir 2 min.","Add tomatoes, stock, chickpeas, and apricots. Bring to boil.","Reduce heat, cover, and simmer 30–35 min until sweet potato is tender.","Taste and adjust. Serve over couscous with almonds, coriander, and lemon."],
    "macros": {"kcal": 420, "protein": 16, "carbs": 62, "fat": 10},
    "perf_tip": "Dried apricots are one of the best sources of potassium — essential for preventing muscle cramps during high-volume training."
  },

  {
    "id": "veg-chili",
    "name": "Smoky Vegetarian Chili",
    "tier": "batch", "tier_label": "Batch Meal",
    "chef": "Diana Kennedy",
    "description": "Three types of beans, a cocoa secret weapon, and smoky depth. Gets better every day it sits in the fridge.",
    "time": "60 min", "servings": "6",
    "ingredients": ["1 can black beans, drained","1 can kidney beans, drained","1 can pinto beans, drained","2 cans crushed tomatoes","1 cup corn kernels","1 large onion, diced","3 garlic cloves, minced","1 red bell pepper, diced","2 tsp smoked paprika","2 tsp cumin","1 tsp chilli powder","1 tsp dried oregano","1 tbsp cocoa powder","Salt & pepper"],
    "steps": ["Sauté onion and pepper in olive oil over medium heat, 8 min. Add garlic and all spices, fry 1 min.","Add tomatoes, beans, corn, cocoa powder, and 1 cup water. Stir well.","Bring to boil, then reduce to low simmer. Cook uncovered 30–40 min, stirring occasionally.","Serve with sour cream, grated cheese, coriander, and warm cornbread or rice. Freezes 3 months."],
    "macros": {"kcal": 390, "protein": 20, "carbs": 60, "fat": 8},
    "perf_tip": "Three bean types gives a diversified amino acid profile. Cocoa adds theobromine — a vasodilator that improves blood flow and endurance performance."
  },

  {
    "id": "minestrone",
    "name": "Classic Minestrone",
    "tier": "batch", "tier_label": "Batch Meal",
    "chef": "Marcella Hazan",
    "description": "Marcella's golden rule: use what's in season, always finish with good Parmesan, never rush the base.",
    "time": "55 min", "servings": "5–6",
    "ingredients": ["1 can cannellini beans, drained","1 can crushed tomatoes","1.5 litres vegetable stock","1 cup small pasta (ditalini or elbow)","2 carrots, diced","2 celery stalks, diced","1 onion, diced","2 zucchini, diced","1 cup green beans, chopped","3 garlic cloves","1 tsp each dried thyme, rosemary, oregano","2 tbsp olive oil","Parmesan rind (if you have it)","Fresh basil & Parmesan to serve"],
    "steps": ["Heat olive oil. Sauté onion, carrot, and celery 10 min — don't rush the soffritto base.","Add garlic and herbs. Add tomatoes and cook 5 min.","Add stock, Parmesan rind, and all remaining veg. Bring to boil, simmer 20 min.","Add pasta and beans, cook 8–10 more min. Remove rind. Serve with basil and generous Parmesan."],
    "macros": {"kcal": 350, "protein": 14, "carbs": 56, "fat": 8},
    "perf_tip": "Tip: add the pasta fresh when reheating each portion to prevent it going mushy. The variety of vegetables here provides a wide spectrum of micronutrients."
  },

  {
    "id": "tomato-bean-soup",
    "name": "Roasted Tomato & White Bean Soup",
    "tier": "batch", "tier_label": "Batch Meal",
    "chef": "Ina Garten",
    "description": "Roasting the tomatoes first concentrates their sweetness and depth dramatically. Restaurant-quality results from humble ingredients.",
    "time": "65 min", "servings": "4–5",
    "ingredients": ["1kg vine tomatoes, halved","2 cans cannellini beans, drained","1 litre vegetable stock","1 head of garlic","1 onion, quartered","3 tbsp olive oil","1 tsp dried thyme","Pinch of chilli flakes","Fresh basil","Parmesan to serve","Good sourdough for dipping"],
    "steps": ["Preheat oven to 200°C. Arrange tomatoes and onion on a baking tray. Slice the top off the garlic head and drizzle with olive oil. Roast everything 35–40 min.","Squeeze roasted garlic cloves out of skins. Blend tomatoes, onion, garlic with half the stock until smooth.","Pour into pot with remaining stock and beans. Simmer 15 min. Season generously.","Serve with torn basil, Parmesan, and sourdough for dipping."],
    "macros": {"kcal": 360, "protein": 16, "carbs": 48, "fat": 12},
    "perf_tip": "Roasting concentrates lycopene — a powerful antioxidant linked to faster recovery. Fat from olive oil increases lycopene absorption."
  },

  {
    "id": "veg-biryani",
    "name": "Vegetable Biryani",
    "tier": "batch", "tier_label": "Batch Meal",
    "chef": "Madhur Jaffrey",
    "description": "An act of love — layered rice, caramelised onions, and fragrant whole spices. The dum (sealed) method makes this unlike any rice dish you've made.",
    "time": "70 min", "servings": "5–6",
    "ingredients": ["2.5 cups basmati rice, washed & soaked 30 min","2 cups mixed veg (cauliflower, peas, carrot, potato)","2 large onions, thinly sliced","½ cup Greek yogurt","Pinch of saffron in 3 tbsp warm milk","4 garlic cloves + 1 inch ginger (blended to paste)","4 cardamom pods, 2 bay leaves, 1 cinnamon stick, 4 cloves (whole)","1.5 tsp biryani masala","Ghee + neutral oil","Fresh mint and coriander"],
    "steps": ["Fry sliced onions in ghee + oil over medium heat until deep golden, 20 min. Set aside half for garnish.","Marinate vegetables in yogurt, garlic-ginger paste, biryani masala, salt for 30 min.","Par-cook rice with whole spices and salt until 70% done (7 min). Drain.","Cook marinated veg in the same pot until half-done. Layer rice over veg. Drizzle saffron milk and fried onions. Seal pot tightly with foil + lid. Cook on low 25 min. Rest 10 min before opening."],
    "macros": {"kcal": 480, "protein": 14, "carbs": 80, "fat": 12},
    "perf_tip": "Basmati has one of the lowest GIs among rice varieties. The ~80g carb per serving is ideal for carb-loading before an endurance event."
  },

  {
    "id": "kale-salad",
    "name": "Quinoa & Kale Power Salad (Meal Prep)",
    "tier": "batch", "tier_label": "Batch Meal",
    "chef": "Yotam Ottolenghi",
    "description": "Gets better as it sits — massaged kale softens and absorbs the dressing. Prep Sunday, eat all week. The ultimate training-week staple.",
    "time": "30 min prep", "servings": "5 (keeps 5 days)",
    "ingredients": ["2 cups quinoa, cooked & cooled","1 large bunch kale, stems removed, leaves torn","2 cans chickpeas, drained & patted dry","1 cup shredded red cabbage","½ cup dried cranberries","½ cup toasted pepitas (pumpkin seeds)","100g feta, crumbled","For dressing: 3 tbsp tahini, 3 tbsp lemon juice, 1 garlic clove, 2 tbsp olive oil, 2 tbsp water, 1 tsp maple syrup, salt"],
    "steps": ["Whisk together all dressing ingredients until smooth. Taste — it should be lemony and nutty.","Place kale in a large bowl. Add 2 tbsp dressing and massage firmly with hands for 2–3 min until kale darkens and softens.","Add quinoa, chickpeas, cabbage, cranberries, and pepitas. Toss with remaining dressing.","Top with feta. Portion into 5 containers. Keeps 5 days in the fridge."],
    "macros": {"kcal": 440, "protein": 18, "carbs": 54, "fat": 18},
    "perf_tip": "Massaging kale breaks down tough cell walls and increases bioavailability of its vitamins — especially K2, which aids calcium metabolism in bones."
  },

  # ── SNACKS ─────────────────────────────────────────────────────────────────

  {
    "id": "roasted-chickpeas",
    "name": "Spiced Roasted Chickpeas",
    "tier": "snack", "tier_label": "Snack",
    "chef": "Yotam Ottolenghi",
    "description": "Crispy, protein-packed, and endlessly variable. Make a batch and keep in an airtight jar for up to a week.",
    "time": "30 min (makes 4 servings)", "servings": "¼ cup",
    "ingredients": ["1 can chickpeas, drained, rinsed & well dried","1 tbsp olive oil","½ tsp smoked paprika","½ tsp cumin","¼ tsp cayenne","½ tsp sea salt"],
    "steps": ["Preheat oven to 220°C. Pat chickpeas completely dry — the drier the better for crunch.","Toss with olive oil and spices. Spread on a baking tray in a single layer.","Roast 25–28 min, shaking halfway, until deep golden and crispy. Cool before eating (they crisp up further as they cool)."],
    "macros": {"kcal": 130, "protein": 6, "carbs": 18, "fat": 4},
    "perf_tip": "One of the best portable protein snacks. Eat 1–2 hours before training for a slow-release energy boost."
  },

  {
    "id": "rice-cakes-hummus",
    "name": "Rice Cakes with Hummus & Cucumber",
    "tier": "snack", "tier_label": "Snack",
    "chef": "Ina Garten",
    "description": "Effortless and deeply satisfying. The ultimate no-fridge-needed snack for between training sessions.",
    "time": "2 min", "servings": "1",
    "ingredients": ["2 brown rice cakes","3 tbsp hummus","½ cucumber, thinly sliced","Pinch of smoked paprika","Drizzle of olive oil","Pinch of sea salt"],
    "steps": ["Spread hummus thickly on each rice cake.","Layer cucumber slices over the top.","Dust with smoked paprika, drizzle olive oil, and add a pinch of sea salt."],
    "macros": {"kcal": 180, "protein": 6, "carbs": 26, "fat": 6},
    "perf_tip": "Rice cakes have a high GI, making them ideal 30–45 min before a workout when you need quick fuel without a heavy stomach."
  },

  {
    "id": "trail-mix",
    "name": "Performance Trail Mix",
    "tier": "snack", "tier_label": "Snack",
    "chef": "Martha Stewart",
    "description": "Custom-built for endurance athletes. Mix once and portion into small bags for the week — no prep needed on the day.",
    "time": "5 min (makes 8 servings)", "servings": "¼ cup",
    "ingredients": ["1 cup raw almonds","½ cup pepitas (pumpkin seeds)","½ cup walnuts","½ cup dried apricots, halved","¼ cup dark chocolate chips (70%+)","¼ cup dried cranberries"],
    "steps": ["Toast almonds, pepitas, and walnuts in a dry pan over medium heat for 3–4 min until fragrant. Cool completely.","Combine with apricots, chocolate chips, and cranberries in a large bowl.","Portion into ¼ cup servings in small bags or jars. Keeps 2 weeks at room temperature."],
    "macros": {"kcal": 200, "protein": 6, "carbs": 16, "fat": 14},
    "perf_tip": "Almonds and walnuts provide the rare combination of protein, magnesium, and vitamin E — all three are depleted by intense training. The dark chocolate adds iron and mood-supporting flavonoids."
  },

  {
    "id": "apple-almond-butter",
    "name": "Apple Slices & Almond Butter",
    "tier": "snack", "tier_label": "Snack",
    "chef": "Nigella Lawson",
    "description": "Simple, elegant, and surprisingly filling. Nigella's philosophy: the best snacks require no cooking whatsoever.",
    "time": "3 min", "servings": "1",
    "ingredients": ["1 large apple (Fuji or Honeycrisp), sliced","2 tbsp natural almond butter","Pinch of cinnamon","Optional: 1 tsp honey, pinch of sea salt"],
    "steps": ["Slice apple into wedges, removing core.","Spoon almond butter into a small bowl for dipping, or spread directly on each slice.","Dust with cinnamon and a pinch of sea salt to intensify the flavour."],
    "macros": {"kcal": 220, "protein": 6, "carbs": 26, "fat": 12},
    "perf_tip": "Apple's quercetin is a natural anti-inflammatory. Paired with almond butter's vitamin E, this is one of the most evidence-backed post-workout recovery snacks."
  },

  {
    "id": "hard-boiled-eggs",
    "name": "Spiced Hard-Boiled Eggs",
    "tier": "snack", "tier_label": "Snack",
    "chef": "Yotam Ottolenghi",
    "description": "Batch-cook 6 at the start of the week. Ottolenghi's spiced salt transforms the humble boiled egg into something genuinely crave-worthy.",
    "time": "12 min (makes 6)", "servings": "2 eggs",
    "ingredients": ["6 eggs","1 tsp za'atar or everything bagel seasoning","½ tsp smoked paprika","Pinch of sea salt","Olive oil drizzle (optional)"],
    "steps": ["Bring a pot of water to a boil. Gently lower in cold eggs. Cook 10 min for hard-boiled.","Transfer to ice water for 5 min. Peel and store in fridge up to 5 days.","To serve, halve and dust with za'atar and smoked paprika. Drizzle with olive oil."],
    "macros": {"kcal": 160, "protein": 14, "carbs": 1, "fat": 10},
    "perf_tip": "Eggs are the highest-quality protein food on the planet by bioavailability score. Two eggs provide all essential amino acids needed for muscle repair. Batch-cook Monday, eat all week."
  },

  {
    "id": "edamame-salt",
    "name": "Edamame with Chilli Sea Salt",
    "tier": "snack", "tier_label": "Snack",
    "chef": "Nobu Matsuhisa",
    "description": "Nobu's izakaya staple — the gold standard of effortless protein snacks. Frozen edamame takes 5 minutes and delivers more protein than almost any other plant snack.",
    "time": "5 min", "servings": "1",
    "ingredients": ["1 cup frozen edamame (in pods or shelled)","½ tsp flaky sea salt","¼ tsp chilli flakes","Optional: squeeze of lemon or lime"],
    "steps": ["Microwave frozen edamame with a splash of water for 3–4 min, or boil 5 min.","Drain and pat dry.","Toss with sea salt and chilli flakes. Serve immediately with lemon on the side."],
    "macros": {"kcal": 150, "protein": 12, "carbs": 12, "fat": 6},
    "perf_tip": "Edamame is one of the few plant foods with a complete amino acid profile. At 12g protein per cup, it beats most protein bars."
  },

  {
    "id": "cheese-crackers",
    "name": "Cheese & Seed Crackers",
    "tier": "snack", "tier_label": "Snack",
    "chef": "Ina Garten",
    "description": "A smarter, more satisfying version of the classic cheese-and-crackers snack. Use a good sharp cheddar or aged manchego.",
    "time": "3 min", "servings": "1",
    "ingredients": ["4–5 whole-grain seed crackers (e.g. Ryvita seeded)","40g sharp cheddar or manchego, sliced","1 tsp wholegrain mustard or mango chutney","A few slices of cucumber or apple"],
    "steps": ["Arrange crackers on a plate.","Top each with a slice of cheese.","Add a small dot of mustard or chutney and a slice of cucumber or apple."],
    "macros": {"kcal": 210, "protein": 10, "carbs": 18, "fat": 12},
    "perf_tip": "Cheese is an efficient source of calcium and phosphorus — two minerals essential for bone health under training load. The whole-grain crackers add B vitamins for energy metabolism."
  },

  {
    "id": "banana-pb",
    "name": "Banana with Peanut Butter",
    "tier": "snack", "tier_label": "Snack",
    "chef": "Jamie Oliver",
    "description": "Jamie's no-nonsense approach: the simplest things are often the best. The classic athlete's snack for a reason — fast carbs, protein, and healthy fat in one.",
    "time": "1 min", "servings": "1",
    "ingredients": ["1 ripe banana","2 tbsp natural peanut butter","Optional: pinch of sea salt, drizzle of honey"],
    "steps": ["Peel banana.","Dip or spread with peanut butter.","Add a pinch of sea salt to enhance the flavour contrast."],
    "macros": {"kcal": 280, "protein": 8, "carbs": 36, "fat": 12},
    "perf_tip": "Bananas are the most studied pre-workout food — their potassium, B6, and natural sugars support muscle contraction and glycogen synthesis. The peanut butter adds slow-burn fat to extend the energy."
  },

]
